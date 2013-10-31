from collections import Counter, OrderedDict

import Cards, Game, Output, Dice
from Constants import *

def getChoiceFromList(player, prompt, list, noChoices=1):
    Output.menuWindow.clear()
    Output.printToWindow(prompt + '\n', Output.menuWindow)

    invalidActions = player._determineValidOptions(list)
    freeActions = player._determineFreeOptions(list)

    count = 1
    indexMapping = {}
    for i, currOption in enumerate(list):
        if currOption in invalidActions.keys():
            Output.printToWindow('{0:2d} - {1} - {2}\n'.format(count, currOption, invalidActions.get(currOption)), Output.menuWindow, colorPair=1)
        elif currOption in freeActions.keys():
            Output.printToWindow('{0:2d} - {1}\n'.format(count, currOption), Output.menuWindow, colorPair=2)
            indexMapping[count] = currOption
        else:
            Output.printToWindow('{0:2d} - {1}\n'.format(count, currOption), Output.menuWindow)
            indexMapping[count] = currOption
        count += 1
    chosenOption = []
    while True:
        for i in range(0, noChoices):
            Output.printToWindow('%d of %d : '%(i, noChoices), Output.menuWindow)
            choice = int(Output.menuWindow.getstr(2))
            #choice -= 48
            if choice >= 1 and choice <= len(list):
                if choice in indexMapping:
                    if noChoices > 1:
                        chosenOption.append(indexMapping[int(choice)])
                    else:
                        chosenOption = indexMapping[int(choice)]
        if len(chosenOption) > 0:
            return chosenOption
def getChoiceFromStack(prompt, currStack, noChoices=1):
    Output.menuWindow.clear()
    Output.printToWindow(prompt + '\n', Output.menuWindow)

    count = 1
    indexMapping = {}
    for i, currCard in enumerate(currStack.cards):
        Output.printToWindow('{0:2d} - {1}\n'.format(count, currCard.visibleName()), Output.menuWindow)
        indexMapping[count] = currCard.name
        count += 1
    chosenCard = []

    while True:
        for i in range(0, noChoices):
            Output.printToWindow('%d of %d : '%(i, noChoices), Output.menuWindow)
            choice = int(Output.menuWindow.getstr(2))
            #choice -= 48
            if choice >= 1 and choice <= len(currStack.cards):
                if choice in indexMapping:
                    chosenCard.append(indexMapping[choice])
        if len(chosenCard) > 0:
            return chosenCard

class Player:
    def __init__(self, name):
        self.name = name
        self.directorStack = Cards.Deck([])
        self.actorStack = Cards.Deck([])
        self.writerStack = Cards.Deck([])
        self.scriptStack = Cards.Deck([])
        self.crewStack = Cards.Deck([])
        self.employeeStack = Cards.Deck(self.directorStack.cards + self.actorStack.cards + self.writerStack.cards + self.crewStack.cards)
        self.productionStack = [Cards.Deck([]), Cards.Deck([])] # B, A
        self.boxOfficeStack = [Cards.Deck([]), Cards.Deck([])]
        self.archiveStack = Cards.Deck([])
        self.theaterStack = Cards.Deck([])
        self.money = 40000
        self.prestige = 0
        self.statuettes = 2
        self.oscars = 0
        self.studio = None
        self.boxOfficeEarnings = 0
        self.noMoviesProduced = 0
        self.yearStatus = {}
        self.phaseStatus = {}
        self.currFreeActions = []
    def _addMoney(self, amount):
        self.money += amount
        return self.money
    def _delMoney(self, amount):
        self.money -= amount
        return self.money
    def _countSalaries(self):
        salaryPayments = 0
        for currCard in self.directorStack.cards:
            salaryPayments += currCard.salary
        for currCard in self.actorStack.cards:
            salaryPayments += currCard.salary[currCard.status]
        for currCard in self.writerStack.cards:
            salaryPayments += currCard.salary
        for currCard in self.crewStack.cards:
            salaryPayments += currCard.salary
        return salaryPayments
    def _countUpkeep(self):
        upkeepPayments = 0
        for currTheater in self.theaterStack:
            if currTheater.status == OPEN:
                upkeepPayments += THEATERUPKEEP
        return upkeepPayments
    def _updateEmployeeStack(self):
        self.employeeStack = Cards.Deck(self.directorStack.cards + self.actorStack.cards + self.writerStack.cards + self.crewStack.cards)
        return True
    def _checkValidScript(self, script, actorStack):
        currActorTypes = []

        for currActor in actorStack.cards:
            currActorTypes.append(currActor.type)

        diff = Counter(script.actors) - Counter(currActorTypes)
        if list(diff.elements()) == []:
            return True

        if QL in currActorTypes:
            # Check if QL can be used as SW
            currActorTypes.remove(QL)
            currActorTypes.append(SW)
            diff = Counter(script.actors) - Counter(currActorTypes)
            if list(diff.elements()) == []:
                return True
            # Check if QL can be used as S
            currActorTypes.remove(SW)
            currActorTypes.append(S)
            diff = Counter(script.actors) - Counter(currActorTypes)
            if list(diff.elements()) == []:
                return True
        return False
    def _addFreeActions(self, actionList):
        if self.statuettes >= 2:
            if ACTTRADE2STAT not in actionList:
                actionList.append(ACTTRADE2STAT)
            if ACTTRADE1STAT not in actionList:
                actionList.append(ACTTRADE1STAT)
        elif self.statuettes == 1:
            if ACTTRADE1STAT not in actionList:
                actionList.append(ACTTRADE1STAT)
        return actionList

    # Decision Making methods
    def _choiceUpkeepPhase(self, actionList):
        return getChoiceFromList(self, 'UPKEEP PHASE', actionList)
    def _choiceUpkeepPaySalariesYN(self):
        return getChoiceFromList(self, 'PAY $%d IN SALARIES?'%self._countSalaries(), MENUYESNO)
    def _choiceUpkeepFireEmployee(self):
        return getChoiceFromStack('FIRE AN EMPLOYEE', self.employeeStack)
    def _choiceUpkeepPayUpkeepYN(self):
        return getChoiceFromList(self, 'PAY $%d IN THEATRE UPKEEP?'%self._countUpkeep(), MENUYESNO)
    def _choiceConstructionPhase(self, actionList):
        return getChoiceFromList(self, 'CONSTRUCTION PHASE', actionList)
    def _choiceBuildTheaterYN(self):
        return getChoiceFromList(self, 'CONSTRUCT A THEATER FOR $%d'%THEATERCOST, MENUYESNO)
    def _choiceActionPhase(self, actionList):
        return getChoiceFromList(self, 'ACTION PHASE', actionList)
    def _choiceBuyScriptChoose(self):
        tmpScriptStack = Cards.Deck([])
        tmpScripts = []
        for i in GENRES:
            tmpScripts.append(Game.board.scriptDecks[i].cards[0])
        tmpScriptStack.addCards(Cards.Deck(tmpScripts))
        return getChoiceFromStack('BUY A SCRIPT', tmpScriptStack)
    def _choiceBuyScriptYN(self):
        return getChoiceFromList(self, 'BUY SCRIPT FOR $%d?'%(SCRIPTCOST), MENUYESNO)
    def _choiceDrawActorYN(self):
        return getChoiceFromList(self, 'DRAW AN ACTOR CARD?', MENUYESNO)
    def _choiceBuyActorYN(self, actor):
        return getChoiceFromList(self, 'HIRE %s FOR $%d / YEAR?'%(actor.name, actor.salary[UNKNOWN]), MENUYESNO)
    def _choiceDrawCraftYN(self):
        return getChoiceFromList(self, 'DRAW A CRAFTSMAN CARD?', MENUYESNO)
    def _choiceBuyCraftYN(self, craft):
        return getChoiceFromList(self, 'HIRE %s FOR $%d / YEAR?'%(craft.name, craft.salary[UNKNOWN]), MENUYESNO)
    def _choiceHireOffice(self):
        return getChoiceFromStack('HIRE FROM THE EMPLOYMENT OFFICE', Game.board.employmentOffice)
    def _choiceHireYN(self, employee):
        return getChoiceFromList(self, 'HIRE %s?'%(employee), MENUYESNO)
    def _choiceScriptBook(self, scripts):
        return getChoiceFromStack('BOOK A MOVIE?', scripts)
    def _choiceAorBMovie(self, script):
        return getChoiceFromList(self, 'BOOK %s AS AN A-MOVIE ($%d) OR B-MOVIE ($%d)?'%(script.visibleName(), script.budgetA, script.budgetB), ["A-MOVIE", "B-MOVIE"])
    def _choiceSelectActors(self, script):
        tmpActorNames = getChoiceFromStack('CHOOSE ACTORS - %s'%script.actors, self.actorStack, noChoices=len(script.actors))
        if self._checkValidScript(script, self.actorStack.copyCards(names=tmpActorNames)):
            return tmpActorNames
        else:
            return False
    def _choiceSelectDirector(self):
        return getChoiceFromStack('CHOOSE A DIRECTOR', self.directorStack)
    def _choicePrivateBookingPhase(self, actionList):
        return getChoiceFromList(self, 'PRIVATE BOOKING PHASE', actionList)

    def _determineValidOptions(self, actionList):
        invalidActionList = {}
        for currAction in actionList:
            # UPKEEP PHASE
            if   currAction == ACTCLAIMSCRIPTS and SCRIPTSCLAIMED in self.yearStatus:
                invalidActionList[ACTCLAIMSCRIPTS] = 'Scripts already Claimed'
            elif currAction == ACTPAYSALARIES and len(self.employeeStack.cards) == 0:
                invalidActionList[ACTPAYSALARIES] = 'No Employees'
            elif currAction == ACTFIREEMPLOY and len(self.employeeStack.cards) == 0:
                invalidActionList[ACTFIREEMPLOY] = 'No Employees'
            elif currAction == ACTOPENTHEATER and len([i for i in self.theaterStack.cards if i.status == OPEN]) == 0:
                invalidActionList[ACTOPENTHEATER] = 'No Closed Theaters'
            elif currAction == ACTCLOSETHEATER and len([i for i in self.theaterStack.cards if i.status == OPEN]) == 0:
                invalidActionList[ACTCLOSETHEATER] = 'No Open Theaters'
            elif currAction == ACTPHASESKIP and EMPLOYEESPAID not in self.yearStatus:
                invalidActionList[ACTPHASESKIP] = 'Need to pay your Employes first'
            elif len(self.theaterStack.cards) == 0:
                invalidActionList.update({ACTPAYUPKEEP: 'No Theaters', ACTCLOSETHEATER: 'No Theaters', ACTSELLTHEATER: 'No Theaters'})

            if self.yearStatus.get(EMPLOYEESPAID):
                invalidActionList.update({ACTPAYSALARIES: 'Already Paid', ACTFIREEMPLOY: 'Already Paid'})
            if self.yearStatus.get(UPKEEPPAID):
                invalidActionList.update({ACTCLOSETHEATER: 'Already Paid', ACTPAYUPKEEP: 'Already Paid'})

            # CONSTRUCTION PHASE
            if self.phaseStatus.get(THEATERBOUGHT):
                invalidActionList.update({ACTBUILDTHEATER: 'Already bought this phase.'})

            # ACTION PHASE
            if Game.board.theaterStack.cards[0].movies.countCards() == Game.board.theaterStack.cards[0].screens:
                invalidActionList[ACTPUBLICBOOK] = 'No Screens Available'
            elif Game.board.employmentOffice.countCards() == 0:
                invalidActionList[ACTHIREOFFICE] = 'No Employees Available'

            # PRIVATE BOOKING PHASE
            tmpScreens = False
            for i in self.theaterStack.cards:
                if i.movies.countCards() < i.screens:
                    tmpScreens = True
            if tmpScreens == False:
                invalidActionList[ACTPRIVATEBOOK] = 'No Screens Available'
            if len(self.theaterStack.cards) == 0:
                invalidActionList[ACTPRIVATEBOOK] = 'No Private Theater'

        return invalidActionList
    def _determineFreeOptions(self, actionList):
        freeActionList = {}
        for currAction in actionList:
            if currAction in ACTFREEACTIONS:
                freeActionList.update({currAction: 'Free'})
            if currAction == ACTPHASESKIP:
                freeActionList.update({ACTPHASESKIP: 'Free'})
        return freeActionList

    # Action methods
    def doUpkeepPhase(self):
        self.yearStatus = {}

        phaseActions = UPKPHASEACTIONS + [ACTPHASESKIP]
        availableActions = phaseActions

        while availableActions != []:
            availableActions = self._addFreeActions(phaseActions)
            self._updateEmployeeStack()

            action = self._choiceUpkeepPhase(availableActions)
            Output.updateScreen()

            if action == ACTCLAIMSCRIPTS:
                for i in self.writerStack.cards:
                    if i.type == ORDINARYWRITER:
                        while True:
                            currGenre = Dice.genreDie.roll()
                            if Game.board.scriptDecks[i].countCards() > 0:
                                self.scriptStack.addCards(Game.board.scriptDecks[i].drawCards(names=currScriptName))
                                self.scriptStack.flipAll(FACEUP)
                                break
                    else:
                        currScriptName = self._choiceBuyScriptChoose()[0]
                        for i in GENRES:
                            if Game.board.scriptDecks[i].cards[0].name == currScriptName:
                                self.scriptStack.addCards(Game.board.scriptDecks[i].drawCards(names=currScriptName))
                                self.scriptStack.flipAll(FACEUP)
                self.yearStatus[SCRIPTSCLAIMED] = True

            elif action == ACTPAYSALARIES:
                if self._choiceUpkeepPaySalariesYN() == YES:
                    self._delMoney(self._countSalaries())
                    self.yearStatus[EMPLOYEESPAID] = True

            elif action == ACTFIREEMPLOY:
                for currEmployeeName in self._choiceUpkeepFireEmployee():
                    # Add Employee to Employment Office
                    employeeList = self.employeeStack.drawCards(names=currEmployeeName)
                    for currEmployee in employeeList.cards:
                        if currEmployee.cardType == DIRECTORCARD:
                            Game.board.employmentOffice.addCards(self.directorStack.drawCards(names=currEmployeeName))
                        elif currEmployee.cardType == ACTORCARD:
                            Game.board.employmentOffice.addCards(self.actorStack.drawCards(names=currEmployeeName))
                        elif currEmployee.cardType == WRITERCARD:
                            Game.board.employmentOffice.addCards(self.writerStack.drawCards(names=currEmployeeName))
                        elif currEmployee.cardType == CREWCARD:
                            Game.board.employmentOffice.addCards(self.crewStack.drawCards(names=currEmployeeName))
                self._updateEmployeeStack()

            elif action == ACTPAYUPKEEP:
                if self._choiceUpkeepPayUpkeepYN() == YES:
                    self._delMoney(self._countUpkeep())
                    self.yearStatus[UPKEEPPAID] = True
                else:
                    action = ACTCLOSETHEATER

            elif action == ACTOPENTHEATER:
                for currTheaterIndex in self._choiceUpkeepOpenTheater():
                    self._delMoney(THEATERUPKEEP + THEATERREOPEN)
                    self.theaterStack.cards[currTheaterIndex].status == OPEN

            elif action == ACTCLOSETHEATER:
                for currTheaterIndex in self._choiceUpkeepCloseTheater():
                    self.theaterStack.cards[currTheaterIndex].status == CLOSED

            elif action == ACTSELLTHEATER:
                for currTheaterIndex in self._choiceUpkeepCloseTheater():
                    self.theaterStack.drawCards(index=currTheaterIndex)

            elif action == ACTPHASESKIP:
                return True

            Output.updateScreen()

        return True
    def doConstructionPhase(self):
        self.phaseStatus = {}

        phaseActions = CONPHASEACTIONS + self.currFreeActions + [ACTPHASESKIP]
        availableActions = phaseActions

        while availableActions != []:
            availableActions = self._addFreeActions(phaseActions)
            action = self._choiceConstructionPhase(availableActions)
            Output.updateScreen()
            if action == ACTBUILDTHEATER:
                if self._choiceBuildTheaterYN() == YES:
                    self._delMoney(THEATERCOST)
                    self.theaterStack.addCards(Cards.Deck([Cards.Theater(type=PRIVATE, screens=3, status=OPEN)]))
                    self.phaseStatus[THEATERBOUGHT] = True
            elif action == ACTPHASESKIP:
                return True
            Output.updateScreen()
        return True
    def doActionPhase(self):
        phaseActions = ACTPHASEACTIONS + self.currFreeActions + [ACTPHASESKIP]
        availableActions = phaseActions

        while availableActions != []:
            availableActions = self._addFreeActions(phaseActions)
            action = self._choiceActionPhase(availableActions)
            Output.updateScreen()

            if action == ACTBUYSCRIPT:
                currScriptName = self._choiceBuyScriptChoose()[0]
                for i in GENRES:
                    if Game.board.scriptDecks[i].cards[0].name == currScriptName:
                        if self._choiceBuyScriptYN() == YES:
                            self._delMoney(SCRIPTCOST)
                            self.scriptStack.addCards(Game.board.scriptDecks[i].drawCards(names=currScriptName))
                            self.scriptStack.flipAll(FACEUP)

                            Output.updateScreen()
                            return True

            elif action == ACTDRAWACTOR:
                if self._choiceDrawActorYN() == YES:
                    tmpHand = Game.board.actorsDeck.drawCards()
                    if self._choiceBuyActorYN(tmpHand.cards[0]) == YES:
                        self.actorStack.addCards(tmpHand)
                    else:
                        Game.board.employmentOffice.addCards(tmpHand)

                    Output.updateScreen()
                    return True

            elif action == ACTDRAWCRAFT:
                if self._choiceDrawCraftYN() == YES:
                    tmpHand = Game.board.actorsDeck.drawCards()
                    if self._choiceBuyCraftYN(tmpHand.cards[0]) == YES:
                        if tmpHand.cards[0].cardType == DIRECTORCARD:
                            self.directorStack.addCards(tmpHand)
                        elif tmpHand.cards[0].cardType == WRITERCARD:
                            self.writerStack.addCards(tmpHand)
                        elif tmpHand.cards[0].cardType == CREWCARD:
                            self.crewStack.addCards(tmpHand)
                    else:
                        Game.board.employmentOffice.addCards(tmpHand)

                    Output.updateScreen()
                    return True

            elif action == ACTHIREOFFICE:
                currHire = self._choiceHireOffice()[0][0]
                if self._choiceHireYN(currHire) == YES:
                    tmpHand = Game.board.employmentOffice.drawCards(names=currHire)
                    if tmpHand.cards[0].cardType == DIRECTORCARD:
                        self.directorStack.addCards(tmpHand)
                    elif tmpHand.cards[0].cardType == WRITERCARD:
                        self.writerStack.addCards(tmpHand)
                    elif tmpHand.cards[0].cardType == CREWCARD:
                        self.crewStack.addCards(tmpHand)
                    elif tmpHand.cards[0].cardType == ACTORCARD:
                        self.actorStack.addCards(tmpHand)

                    Output.updateScreen()
                    return True

            elif action == ACTPUBLICBOOK:
                validScripts = []
                for i in self.scriptStack.cards:
                    if self._checkValidScript(i, self.actorStack):
                        validScripts.append(i)
                if len(validScripts) > 0:
                    currScriptName = self._choiceScriptBook(Cards.Deck(validScripts))[0]
                    if self.directorStack.countCards() > 0:
                        tmpMovie = Cards.Movie(currScriptName)
                        tmpMovie.scriptStack = self.scriptStack.drawCards(names=currScriptName)
                        tmpDirector = self._choiceSelectDirector()
                        tmpMovie.directorStack.addCards(self.directorStack.drawCards(names=tmpDirector))
                        tmpActors = self._choiceSelectActors(tmpMovie.scriptStack.cards[0])
                        if tmpActors:
                            tmpMovie.actorStack.addCards(self.actorStack.drawCards(names=tmpActors))
                            tmpType = self._choiceAorBMovie(tmpMovie.scriptStack.cards[0])
                            if tmpType == "A-MOVIE":    tmpMovie.type = AMOVIE
                            elif tmpType == "B-MOVIE":  tmpMovie.type = BMOVIE
                            if Game.board.theaterStack.cards[0].bookMovie(Cards.Deck([tmpMovie])):
                                self._delMoney(1000)
                                self.productionStack[tmpMovie.type].addCards(Cards.Deck([tmpMovie]));
                                Output.printToWindow('MOVIE BOOKED', Output.menuWindow)

                                Output.updateScreen()
                                return True
                        else:
                            self.scriptStack.addCards(tmpMovie.scriptStack)
                            self.directorStack.addCards(tmpMovie.directorStack)
                            self.actorStack.addCards(tmpMovie.actorStack)
                            Output.printToWindow('INVALID SELECTION', Output.menuWindow)
                    else:
                        Output.printToWindow('NO DIRECTORS AVAILABLE', Output.menuWindow)
                else:
                    Output.printToWindow('NO VALID SCRIPTS', Output.menuWindow)

            elif action == ACTPHASESKIP:
                Output.updateScreen()
                return True

        Output.updateScreen()
        return True
    def doPrivateBookingPhase(self):
        phaseActions = PVTPHASEACTIONS + self.currFreeActions + [ACTPHASESKIP]
        availableActions = phaseActions

        while availableActions != []:
            availableActions = self._addFreeActions(phaseActions)
            action = self._choicePrivateBookingPhase(availableActions)
            Output.updateScreen()
            if action == ACTPRIVATEBOOK:
                validScripts = []
                for i in self.scriptStack.cards:
                    if self._checkValidScript(i, self.actorStack):
                        validScripts.append(i)
                if len(validScripts) > 0:
                    currScriptName = self._choiceScriptBook(Cards.Deck(validScripts))[0]
                    if self.directorStack.countCards() > 0:
                        tmpMovie = Cards.Movie(currScriptName)
                        tmpMovie.scriptStack = self.scriptStack.drawCards(names=currScriptName)
                        tmpDirector = self._choiceSelectDirector()
                        tmpMovie.directorStack.addCards(self.directorStack.drawCards(names=tmpDirector))
                        tmpActors = self._choiceSelectActors(tmpMovie.scriptStack.cards[0])
                        if tmpActors:
                            tmpMovie.actorStack.addCards(self.actorStack.drawCards(names=tmpActors))
                            tmpType = self._choiceAorBMovie(tmpMovie.scriptStack.cards[0])
                            if tmpType == "A-MOVIE":    tmpMovie.type = AMOVIE
                            elif tmpType == "B-MOVIE":  tmpMovie.type = BMOVIE
                            for i in self.theaterStack.cards:
                                if i.bookMovie(Cards.Deck([tmpMovie])):
                                    self.productionStack[tmpMovie.type].addCards(Cards.Deck([tmpMovie]));
                                    Output.printToWindow('MOVIE BOOKED', Output.menuWindow)

                                    Output.updateScreen()
                                    return True
                        else:
                            self.scriptStack.addCards(tmpMovie.scriptStack)
                            self.directorStack.addCards(tmpMovie.directorStack)
                            self.actorStack.addCards(tmpMovie.actorStack)
                            Output.printToWindow('INVALID SELECTION', Output.menuWindow)
                    else:
                        Output.printToWindow('NO DIRECTORS AVAILABLE', Output.menuWindow)
                else:
                    Output.printToWindow('NO VALID SCRIPTS', Output.menuWindow)
            elif action == ACTPHASESKIP:
                Output.updateScreen()
                return True
        Output.updateScreen()
        return True
