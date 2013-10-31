from collections import Counter, OrderedDict

import Cards, Game, Output
from Constants import *

# def getChoiceFromList(prompt, list, noChoices=1):
#     print prompt
#     count = 1
#     indexMapping = {}
#     for i, currOption in enumerate(list):
#         print '{0:2d} - {1}'.format(count, currOption)
#         indexMapping[count] = currOption
#         count += 1
#     if noChoices > 1:
#         chosenOption = []
#     else:
#         chosenOption = None
#     while True:
#         for i in range(0, noChoices):
#             choice = input('%d of %d :'%(i, noChoices))
#             if choice >= 1 and choice <= len(list):
#                 if choice in indexMapping:
#                     if noChoices > 1:
#                         chosenOption.append(indexMapping[int(choice)])
#                     else:
#                         chosenOption = indexMapping[int(choice)]
#         if chosenOption:
#             return chosenOption
# def getChoiceFromStack(prompt, currStack, noChoices=1):
#     print prompt
#     count = 1
#     indexMapping = {}
#     for i, currCard in enumerate(currStack.cards):
#         print '{0:2d} - {1}'.format(count, currCard.visibleName())
#         indexMapping[count] = currCard.name
#         count += 1
#     chosenCard = []

#     for i in range(0, noChoices):
#         choice = input('%d of %d :'%(i, noChoices))
#         if choice >= 1 and choice <= len(currStack.cards):
#             if choice in indexMapping:
#                 chosenCard.append(indexMapping[choice])
#     if chosenCard:
#         return chosenCard
#     else:
#         return False

def getChoiceFromList(player, prompt, list, noChoices=1):
    Output.menuWindow.clear()
    Output.printToWindow(prompt + '\n', Output.menuWindow)

    invalidActions = player._determineValidOptions(list)

    count = 1
    indexMapping = {}
    for i, currOption in enumerate(list):
        if currOption in invalidActions.keys():
            Output.printToWindow('{0:2d} - {1} - {2}\n'.format(count, currOption, invalidActions.get(currOption)), Output.menuWindow, colorPair=1)
        else:
            Output.printToWindow('{0:2d} - {1}\n'.format(count, currOption), Output.menuWindow)
            indexMapping[count] = currOption
        count += 1
    if noChoices > 1:
        chosenOption = []
    else:
        chosenOption = None
    while True:
        for i in range(0, noChoices):
            Output.printToWindow('%d of %d : '%(i, noChoices), Output.menuWindow)
            choice = Output.menuWindow.getch()
            choice -= 48
            if choice >= 1 and choice <= len(list):
                if choice in indexMapping:
                    if noChoices > 1:
                        chosenOption.append(indexMapping[int(choice)])
                    else:
                        chosenOption = indexMapping[int(choice)]
        if chosenOption:
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

    for i in range(0, noChoices):
        Output.printToWindow('%d of %d : '%(i, noChoices), Output.menuWindow)
        choice = Output.menuWindow.getch()
        choice -= 48
        if choice >= 1 and choice <= len(currStack.cards):
            if choice in indexMapping:
                chosenCard.append(indexMapping[choice])
    if chosenCard:
        return chosenCard
    else:
        return False

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
        self.statuettes = 0
        self.oscars = 0
        self.studio = None
        self.boxOfficeEarnings = 0
        self.noMoviesProduced = 0
        self.turnStatus = {}
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
    def _choiceScriptPublicBook(self, scripts):
        return getChoiceFromStack('BOOK A MOVIE?', scripts)
    def _choiceSelectActors(self, script):
        tmpActorNames = getChoiceFromStack('CHOOSE ACTORS - %s'%script.actors, self.actorStack, noChoices=len(script.actors))
        if self._checkValidScript(script, self.actorStack.copyCards(names=tmpActorNames)):
            return tmpActorNames
        else:
            return False
    def _choiceSelectDirector(self):
        return getChoiceFromStack('CHOOSE A DIRECTOR', self.directorStack)

    def _determineValidOptions(self, actionList):
        invalidActionList = {}
        for currAction in actionList:
            # UPKEEP PHASE
            if   currAction == ACTPAYSALARIES and len(self.employeeStack.cards) == 0:
                invalidActionList[ACTPAYSALARIES] = 'No Employees'
            elif currAction == ACTFIREEMPLOY and len(self.employeeStack.cards) == 0:
                invalidActionList[ACTFIREEMPLOY] = 'No Employees'
            elif currAction == ACTOPENTHEATER and len([i for i in self.theaterStack.cards if i.status == OPEN]) == 0:
                invalidActionList[ACTOPENTHEATER] = 'No Closed Theaters'
            elif currAction == ACTCLOSETHEATER and len([i for i in self.theaterStack.cards if i.status == OPEN]) == 0:
                invalidActionList[ACTCLOSETHEATER] = 'No Open Theaters'
            elif currAction == ACTPHASESKIP and EMPLOYEESPAID not in self.turnStatus:
                invalidActionList[ACTPHASESKIP] = 'Need to pay your Employes first'
            elif len(self.theaterStack.cards) == 0:
                invalidActionList.update({ACTPAYUPKEEP: 'No Theaters', ACTCLOSETHEATER: 'No Theaters', ACTSELLTHEATER: 'No Theaters'})

            if self.turnStatus.get(EMPLOYEESPAID):
                invalidActionList.update({ACTPAYSALARIES: 'Already Paid', ACTFIREEMPLOY: 'Already Paid'})
            if self.turnStatus.get(UPKEEPPAID):
                invalidActionList.update({ACTCLOSETHEATER: 'Already Paid', ACTPAYUPKEEP: 'Already Paid'})

            # ACTION PHASE
            if Game.board.theaterStack.cards[0].movies.countCards() == Game.board.theaterStack.cards[0].screens:
                invalidActionList[ACTPUBLICBOOK] = 'No Screens Available'
            elif Game.board.employmentOffice.countCards() == 0:
                invalidActionList[ACTHIREOFFICE] = 'No Employees Available'

        return invalidActionList

    # Action methods
    def doUpkeepPhase(self):
        self.turnStatus = {}

        availableActions = UPKPHASEACTIONS + [ACTPHASESKIP]

        while availableActions != []:
            self._updateEmployeeStack()

            action = self._choiceUpkeepPhase(availableActions)
            Output.updateScreen()

            if action == ACTPAYSALARIES:
                if self._choiceUpkeepPaySalariesYN() == YES:
                    self._delMoney(self._countSalaries())
                    self.turnStatus[EMPLOYEESPAID] = True

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
                    self.turnStatus[UPKEEPPAID] = True
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
        availableActions = CONPHASEACTIONS + [ACTPHASESKIP]

        while availableActions != []:
            action = self._choiceConstructionPhase(availableActions)
            Output.updateScreen()
            if action == ACTBUILDTHEATER:
                if self._choiceBuildTheaterYN() == YES:
                    self._delMoney(THEATERCOST)
                    self.theaterStack.addCards(Cards.Deck([Cards.Theater(type=PRIVATE, screens=3, status=OPEN)]))
            elif action == ACTPHASESKIP:
                return True
            Output.updateScreen()
        return True
    def doActionPhase(self):
        availableActions = ACTPHASEACTIONS

        while availableActions != []:
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
                            return True

            elif action == ACTDRAWACTOR:
                if self._choiceDrawActorYN() == YES:
                    tmpHand = Game.board.actorsDeck.drawCards()
                    if self._choiceBuyActorYN(tmpHand.cards[0]) == YES:
                        self.actorStack.addCards(tmpHand)
                    else:
                        Game.board.employmentOffice.addCards(tmpHand)
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
                    return True

            elif action == ACTPUBLICBOOK:
                validScripts = []
                for i in self.scriptStack.cards:
                    if self._checkValidScript(i, self.actorStack):
                        validScripts.append(i)
                if len(validScripts) > 0:
                    currScriptName = self._choiceScriptPublicBook(Cards.Deck(validScripts))[0]
                    if self.directorStack.countCards() > 0:
                        tmpMovie = Cards.Movie(currScriptName)
                        tmpMovie.scriptStack = self.scriptStack.drawCards(names=currScriptName)
                        tmpDirector = self._choiceSelectDirector()
                        tmpMovie.directorStack.addCards(self.directorStack.drawCards(names=tmpDirector))
                        tmpActors = self._choiceSelectActors(tmpMovie.scriptStack.cards[0])
                        if tmpActors:
                            tmpMovie.actorStack.addCards(self.actorStack.drawCards(names=tmpActors))
                            if Game.board.theaterStack.cards[0].bookMovie(Cards.Deck([tmpMovie])):
                                Output.printToWindow('MOVIE BOOKED', Output.menuWindow)
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
                return True
            Output.updateScreen()
        return True
