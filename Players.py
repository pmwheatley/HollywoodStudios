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
            Output.printToWindow('{0:2d} - {1} - {2}\n'.format(count, currOption, freeActions.get(currOption)), Output.menuWindow, colorPair=2)
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
    def __init__(self, name, studio):
        self.name = name
        self.studio = studio
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
        self.boxOfficeEarnings = 0
        self.noMoviesProduced = 0
        self.yearStatus = {}
        self.phaseStatus = {}
        self.currFreeActions = []
        self.abilities = {}

        self._initAbilities()
    def _initAbilities(self):
        if self.studio == MGM:
            self.abilities[AMOVIEFIRSTSTAR] = True
            self.abilities[ALLMOVIEBONUS] = 1
            self.abilities[AMOVIESONLY] = True
            self.abilities[CANTFREEREIGN] = True
        elif self.studio == PAR:
            self.abilities[MUSTFREEREIGN] = True
            self.abilities[BLOCKBOOKING] = True
            self.abilities[BMOVIESONLY] = True
        elif self.studio == FOX:
            self.abilities[BOGENREREROLL] = True
        elif self.studio == UNI:
            self.abilities[HORRORBONUS] = 2
            self.abilities[FREEPUBLICBOOK] = True
            self.abilities[BMOVIEPOLISH] = 2000
            self.abilities[STARLIMIT] = 3
        elif self.studio == WAR:
            self.abilities[MULTIACTIONS] = 2
            self.abilities[FILMNOIRBONUS] = 2
            self.abilities[BMOVIESONLY] = True
        # FOX gets a Free Theater at the start
        if self.studio == FOX:
            self.theaterStack.addCards(Cards.Deck([Cards.Theater(type=PRIVATE, screens=3, status=OPEN)]))
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
    def _addFreeActions(self):
        # TODO: phaseActions not restting?
        actionList = []
        if self.statuettes >= 2:
            if ACTTRADE2STAT not in actionList:
                actionList.append(ACTTRADE2STAT)
            if ACTTRADE1STAT not in actionList:
                actionList.append(ACTTRADE1STAT)
        elif self.statuettes == 1:
            if ACTTRADE1STAT not in actionList:
                actionList.append(ACTTRADE1STAT)
        return actionList

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
            for i in self.scriptStack.cards:
                if self._checkValidScript(i, self.actorStack) == True:
                    if ACTPUBLICBOOK in invalidActionList:
                        del invalidActionList[ACTPUBLICBOOK]
                    break
                else:
                    invalidActionList[ACTPUBLICBOOK] = 'No Valid Scripts'

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
                freeActionList[currAction] = 'Free'
            if currAction == ACTPHASESKIP:
                freeActionList[currAction] = 'Free'
        # ABILITIES - BLOCKBOOKING
        if self.studio == PAR and BLOCKBOOKING in self.abilities:
            freeActionList[ACTPUBLICBOOK] = 'You can book multiple movies'
        return freeActionList

    # Free Action Methods (Trade Statuettes, Play Event Cards etc.)
    def doFreeAction(self, action):
        if action == ACTTRADE2STAT:
            self.statuettes -= 2
        elif action == ACTTRADE1STAT:
            self.statuettes -= 1
        return True
    # Book a movie
    def doBookMovie(self, theatre=PUBLIC):
        validScripts = []
        tmpActors = []
        for i in self.scriptStack.cards:
            if self._checkValidScript(i, self.actorStack):
                validScripts.append(i)
        if len(validScripts) > 0:
            currScriptName = self._choiceScriptBook(Cards.Deck(validScripts))[0]
            if self.directorStack.countCards() > 0:
                tmpMovie = Cards.Movie(currScriptName)
                tmpMovie.scriptStack = self.scriptStack.drawCards(names=currScriptName)
                tmpDirector = self._choiceSelectDirector()
                Output.printToLog(str(tmpDirector))
                tmpMovie.directorStack.addCards(self.directorStack.drawCards(names=tmpDirector))
                tmpActors = self._choiceSelectActors(tmpMovie.scriptStack.cards[0])
                Output.printToLog(str(tmpActors))
                if tmpActors:
                    tmpMovie.actorStack.addCards(self.actorStack.drawCards(names=tmpActors))

                    tmpMovie = self._applyAbilitiesBooking(tmpMovie)

                    Output.printToLog(str(Game.board.theaterStack.cards[0].movies.countCards()))
                    Output.printToLog(str(Game.board.theaterStack.cards[0].screens))

                    if theatre == PUBLIC:
                        if Game.board.theaterStack.cards[0].bookMovie(Cards.Deck([tmpMovie])):
                            # Pay movie budget
                            self._delMoney(tmpMovie.budget)
                            # ABILITIES - FREEPUBLICBOOK
                            if FREEPUBLICBOOK not in self.abilities:
                                self._delMoney(1000)
                            self.productionStack[tmpMovie.type].addCards(Cards.Deck([tmpMovie]));
                            Output.printToLog('MOVIE BOOKED')
                            Output.updateScreen()
                            # ABILITIES - BLOCKBOOKING
                            if BLOCKBOOKING not in self.abilities:
                                return True
                        else:
                            Output.printToLog('NO SCREENS AVAILABLE')
                    elif theatre == PRIVATE:
                        for i in self.theaterStack.cards:
                            if i.bookMovie(Cards.Deck([tmpMovie])):
                                # Pay movie budget
                                self._delMoney(tmpMovie.budget)
                                # ABILITIES - FREEPUBLICBOOK
                                if FREEPUBLICBOOK not in self.abilities:
                                    self._delMoney(1000)
                                self.productionStack[tmpMovie.type].addCards(Cards.Deck([tmpMovie]));
                                Output.printToLog('MOVIE BOOKED')
                                Output.updateScreen()
                                # ABILITIES - BLOCKBOOKING
                                if BLOCKBOOKING not in self.abilities:
                                    return True
                            else:
                                Output.printToLog('NO SCREENS AVAILABLE')
                else:
                    Output.printToLog('INVALID SELECTION')
            else:
                Output.printToLog('NO DIRECTORS AVAILABLE')
        else:
            Output.printToLog('NO VALID SCRIPTS')

        self.scriptStack.addCards(tmpMovie.scriptStack)
        self.directorStack.addCards(tmpMovie.directorStack)
        self.actorStack.addCards(tmpMovie.actorStack)
        return False

    # Director / Studio Abilities
    def _applyAbilitiesBooking(self, movie):

        currGenre = movie.scriptStack.cards[0].genre
        currDirector = movie.directorStack.cards[0]

        # ABILITIES - MUSTFREEREIGN CANTFREEREIGN
        if MUSTFREEREIGN in self.abilities:
            movie.freeReign = True
        elif CANTFREEREIGN in self.abilities:
            movie.freeReign = False
        else:
            freeReign = self._choiceDirectorFreeReign(currDirector.name)
            if freeReign == "Y":        movie.freeReign = True
            elif freeReign == "N":      movie.freeReign = False

        # ABILITIES - AMOVIESONLY BMOVIESONLY
        if AMOVIESONLY in self.abilities:
            movie.type = AMOVIE
        elif BMOVIESONLY in self.abilities:
            movie.type = BMOVIE
        else:
            tmpType = self._choiceAorBMovie(movie.scriptStack.cards[0])
            if tmpType == "A-MOVIE":    movie.type = AMOVIE
            elif tmpType == "B-MOVIE":  movie.type = BMOVIE

        # ABILITIES - BMOVIEPOLISH
        if movie.type == BMOVIE and BMOVIEPOLISH in self.abilities:
            tmpPolish = self._choicePolishMovie()

            if tmpPolish == "Y":
                self._delMoney(2000)
                movie.polished = True

        # ABILITIES - ALLMOVIEBONUS AMOVIEBONUS BMOVIEBONUS
        if ALLMOVIEBONUS in self.abilities:
            movie.initBonus += self.abilities[ALLMOVIEBONUS]
        if ALLMOVIEBONUS in currDirector.abilities:
            movie.initBonus += currDirector.abilities[ALLMOVIEBONUS]

        if movie.type == AMOVIE:
            if AMOVIEBONUS in self.abilities:
                movie.initBonus += self.abilities[AMOVIEBONUS]
            if AMOVIEBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[AMOVIEBONUS]
        elif movie.type == BMOVIE:
            if BMOVIEBONUS in self.abilities:
                movie.initBonus += self.abilities[BMOVIEBONUS]
            if BMOVIEBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[BMOVIEBONUS]

        # ABILITIES - FILMNOIRBONUS  ROMANCEBONUS  HORRORBONUS  COMEDYBONUS  EPICBONUS  SWORDSBONUS
        if currGenre == FILMNOIR:
            if FILMNOIRBONUS in self.abilities:
                movie.initBonus += self.abilities[FILMNOIRBONUS]
            if FILMNOIRBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[FILMNOIRBONUS]
        elif currGenre == ROMANCE:
            if ROMANCEBONUS in self.abilities:
                movie.initBonus += self.abilities[ROMANCEBONUS]
            if ROMANCEBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[ROMANCEBONUS]
        elif currGenre == HORROR:
            if HORRORBONUS in self.abilities:
                movie.initBonus += self.abilities[HORRORBONUS]
            if HORRORBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[HORRORBONUS]
        elif currGenre == COMEDY :
            if COMEDYBONUS in self.abilities:
                movie.initBonus += self.abilities[COMEDYBONUS]
            if COMEDYBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[COMEDYBONUS]
        elif currGenre == EPIC:
            if EPICBONUS in self.abilities:
                movie.initBonus += self.abilities[EPICBONUS]
            if EPICBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[EPICBONUS]
        elif currGenre == SWORDS:
            if SWORDSBONUS in self.abilities:
                movie.initBonus += self.abilities[SWORDSBONUS]
            if SWORDSBONUS in currDirector.abilities:
                movie.initBonus += currDirector.abilities[SWORDSBONUS]

        # ABILITIES - AMOVIEEXTRACOST BMOVIEEXTRACOST
        movie.calcBudget()
        if movie.type == AMOVIE:
            if AMOVIEEXTRACOST in self.abilities:
                movie.budget += self.abilities[AMOVIEEXTRACOST]
            if AMOVIEEXTRACOST in currDirector.abilities:
                movie.budget += currDirector.abilities[AMOVIEEXTRACOST]
        if movie.type == BMOVIE:
            if BMOVIEEXTRACOST in self.abilities:
                movie.budget += self.abilities[BMOVIEEXTRACOST]
            if BMOVIEEXTRACOST in currDirector.abilities:
                movie.budget += currDirector.abilities[BMOVIEEXTRACOST]

        # ABILITIES - ROLLOSCAR
        tmpDie = Dice.Die(3, [1,2,3])
        if ROLLOSCAR in self.abilities or ROLLOSCAR in currDirector.abilities:
            if tmpDie.roll() == 1:
                movie.scriptStack.cards[0].instantClassic = True

        # ABILITIES - FILMNOIRROLLCLASSIC ROMANCEROLLCLASSIC  HORRORROLLCLASSIC  COMEDYROLLCLASSIC  EPICROLLCLASSIC  SWORDSROLLCLASSIC
        if currGenre == FILMNOIR:
            if FILMNOIRROLLCLASSIC in self.abilities or FILMNOIRROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True
        elif currGenre == ROMANCE:
            if ROMANCEROLLCLASSIC in self.abilities or ROMANCEROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True
        elif currGenre == HORROR:
            if HORRORROLLCLASSIC in self.abilities or HORRORROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True
        elif currGenre == COMEDY :
            if COMEDYROLLCLASSIC in self.abilities or COMEDYROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True
        elif currGenre == EPIC:
            if EPICROLLCLASSIC in self.abilities or EPICROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True
        elif currGenre == SWORDS:
            if SWORDSROLLCLASSIC in self.abilities or SWORDSROLLCLASSIC in currDirector.abilities:
                if tmpDie.roll() == 1:
                    movie.scriptStack.cards[0].instantClassic = True

        return movie

    # Action methods
    def doUpkeepPhase(self):
        self.yearStatus = {}
        phaseActions = UPKPHASEACTIONS + [ACTPHASESKIP]
        availableActions = []

        while True:
            availableActions = phaseActions + self._addFreeActions()
            self._updateEmployeeStack()
            action = self._choiceUpkeepPhase(availableActions)
            Output.updateScreen()

            if action in ACTFREEACTIONS:
                self.doFreeAction(action)

            if action == ACTCLAIMSCRIPTS:
                for i in self.writerStack.cards:
                    if i.type == ORDINARYWRITER:
                        while True:
                            currGenre = Dice.genreDie.roll()
                            if Game.board.scriptDecks[currGenre].countCards() > 0:
                                self.scriptStack.addCards(Game.board.scriptDecks[currGenre].drawCards())
                                self.scriptStack.flipAll(FACEUP)
                                break
                    else:
                        currScriptName = self._choiceBuyScriptChoose()[0]
                        for currGenre in GENRES:
                            if Game.board.scriptDecks[currGenre].cards[0].name == currScriptName:
                                self.scriptStack.addCards(Game.board.scriptDecks[currGenre].drawCards(names=currScriptName))
                                self.scriptStack.flipAll(FACEUP)

                # ABILITIES - ALSOWRITER
                for currDirector in self.directorStack.cards:
                    if ALSOWRITER in currDirector.abilities:
                        currScriptName = self._choiceBuyScriptChoose()[0]
                        for currGenre in GENRES:
                            if Game.board.scriptDecks[currGenre].cards[0].name == currScriptName:
                                self.scriptStack.addCards(Game.board.scriptDecks[currGenre].drawCards(names=currScriptName))
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
        availableActions = []

        while True:
            availableActions = phaseActions + self._addFreeActions()
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
        # ABILITIES - MULTIACTIONS
        if MULTIACTIONS in self.abilities:
            for i in range(0, self.abilities[MULTIACTIONS]):
                self.doActionPhaseAction()
        else:
            self.doActionPhaseAction()
        return True
    def doActionPhaseAction(self):
        phaseActions = ACTPHASEACTIONS + self.currFreeActions + [ACTPHASESKIP]
        availableActions = []
        while True:
            availableActions = phaseActions + self._addFreeActions()
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
                    tmpHand = Game.board.craftsDeck.drawCards()
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
                if self.doBookMovie(PUBLIC):
                    return True

            elif action == ACTPHASESKIP:
                Output.updateScreen()
                return True

        Output.updateScreen()
        return True
    def doPrivateBookingPhase(self):
        phaseActions = PVTPHASEACTIONS + self.currFreeActions + [ACTPHASESKIP]
        availableActions = []

        while True:
            availableActions = phaseActions + self._addFreeActions()
            action = self._choicePrivateBookingPhase(availableActions)
            Output.updateScreen()

            if action == ACTPRIVATEBOOK:
                self.doBookMovie(PRIVATE)

            elif action == ACTPHASESKIP:
                Output.updateScreen()
                return True
        Output.updateScreen()
        return True

class HumanPlayer(Player):
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
        return getChoiceFromList(self, 'HIRE %s FOR $%d / YEAR?'%(actor.visibleName(), actor.salary[UNKNOWN]), MENUYESNO)
    def _choiceDrawCraftYN(self):
        return getChoiceFromList(self, 'DRAW A CRAFTSMAN CARD?', MENUYESNO)
    def _choiceBuyCraftYN(self, craft):
        return getChoiceFromList(self, 'HIRE %s FOR $%d / YEAR?'%(craft.name, craft.salary), MENUYESNO)
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
    def _choiceDirectorFreeReign(self, director):
        return getChoiceFromList(self, 'GIVE %s FREE REIGN?'%(director), MENUYESNO)
    def _choicePrivateBookingPhase(self, actionList):
        return getChoiceFromList(self, 'PRIVATE BOOKING PHASE', actionList)
    def _choicePolishMovie(self):
        return getChoiceFromList(self, 'POLISH MOVIE INTO AN A-MOVIE FOR $%d?'%(self.abilities[BMOVIEPOLISH]), MENUYESNO)

class BasicAIPlayer(Player):
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
        return getChoiceFromList(self, 'HIRE %s FOR $%d / YEAR?'%(actor.visibleName(), actor.salary[UNKNOWN]), MENUYESNO)
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
    def _choiceDirectorFreeReign(self, director):
        return getChoiceFromList(self, 'GIVE %s FREE REIGN?'%(director), MENUYESNO)
    def _choicePrivateBookingPhase(self, actionList):
        return getChoiceFromList(self, 'PRIVATE BOOKING PHASE', actionList)
    def _choicePolishMovie(self):
        return getChoiceFromList(self, 'POLISH MOVIE INTO AN A-MOVIE FOR $%d?'%(self.abilities[BMOVIEPOLISH]), MENUYESNO)
