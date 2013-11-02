from Constants import *
import Dice

class Card():
    def __init__(self):
        self.name   = None
        self.id     = None
        self.face   = FACEUP
    def _isValidCard(self):
        if self.name:
            return True
    def flip(self):
        if self.face == FACEUP:
            self.face = FACEDOWN
        else:
            self.face = FACEUP

class Deck():
    def __init__(self, cards=[]):
        self.name       = None
        self.id         = None
        self.cards      = cards
        self.maxCards   = 256
    def _isValidDeck(self):
        return True
    def _findCard(self, name=None, id=None):
        """Return a list of self.cards indices showing card instances with matching id"""
        if name:
            cardIndex = [i for i,x in enumerate(self.cards) if x.name == name]
            return cardIndex[0]
        elif id:
            cardIndex = [i for i,x in enumerate(self.cards) if x.id == id]
            return cardIndex[0]
        else:
            return False
    def _copyMultiple(self, number=1, names=None, ids=None, indices=None):
        if indices == None:
            indices = []
        elif type(indices) is int:
            indices = [indices]
        elif type(indices) is list:
            indices = indices

        if type(names) is str:
            indices.append(self._findCard(name=names))
        elif type(names) is list:
            for i in names:
                indices.append(self._findCard(name=i))
        elif type(ids) is int:
            indices.append(self._findCard(id=ids))
        elif type(ids) is list:
            for i in ids:
                indices.append(self._findCard(id=i))
        elif number == 1:
            indices = [0]
        else:
            indices = range(0, number)

        number = len(indices)

        currentCards = []
        for i in reversed(sorted(indices)):
            currentCards.append(self.cards[i])
        return Deck(currentCards)
    def _drawMultiple(self, number=1, names=None, ids=None, indices=None):
        if indices == None:
            indices = []
        elif type(indices) is int:
            indices = [indices]
        elif type(indices) is list:
            indices = indices

        if type(names) is str:
            indices.append(self._findCard(name=names))
        elif type(names) is list:
            for i in names:
                indices.append(self._findCard(name=i))
        elif type(ids) is int:
            indices.append(self._findCard(id=ids))
        elif type(ids) is list:
            for i in ids:
                indices.append(self._findCard(id=i))
        elif number == 1:
            indices = [0]
        else:
            indices = range(0, number)

        number = len(indices)

        currentCards = []
        for i in reversed(sorted(indices)):
            currentCards.append(self.cards.pop(i))
        return Deck(currentCards)
    def _addMultiple(self, deck=None, toTop=False):
        for i in deck.cards:
            if i._isValidCard():
                pass
            else:
                return False
        else:
            if (self.countCards() < self.maxCards):
                if toTop == True:
                    for i in deck.cards:
                        self.cards.insert(0, i)
                    return True
                else:
                    for i in deck.cards:
                        self.cards.insert(len(self.cards), i)
                    return True
            else:
                return False

    def flipAll(self, face=FACEUP):
        if face == FACEUP or face == FACEDOWN:
            for i in self.cards:
                i.face = face
            return True
        return False
    def shuffle(self):
        Dice.random.shuffle(self.cards)
        return True
    def countCards(self):
        return len(self.cards)
    def isCardInDeck(self, name=None, id=None):
        if name:
            if self.findCardByName(name):
                return True
        if id:
            if self.findCardByID(id):
                return True
        return False
    def copyCards(self, number=None, names=None, ids=None, indices=None):
        if number and (names or ids or indices):
            return False
        elif (names and ids) or (ids and indices) or (indices and names):
            return False
        else:
            return self._copyMultiple(names=names, ids=ids, indices=indices)
    def drawCards(self, number=None, names=None, ids=None, indices=None):
        if number and (names or ids or indices):
            return False
        elif (names and ids) or (ids and indices) or (indices and names):
            return False
        else:
            return self._drawMultiple(names=names, ids=ids, indices=indices)
    def addCards(self, deck, toTop=False):
        if deck._isValidDeck():
            self._addMultiple(deck, toTop)
            return True
        else:
            return False

class ActorCard(Card):
    def __init__(self, id, name, type, salary, bonus):
        self.id = id
        self.name = name
        self.type = type
        self.salary = salary
        self.bonus = bonus
        self.status = UNKNOWN
        self.cardType = ACTORCARD
        self.face = FACEUP
    def upgradeStatus(self):
        if self.status == UNKNOWN:
            self.status = STAR
            return True
        else:
            return False
    def getSalary(self):
        return self.salary[self.status]
    def getBonus(self, movietype):
        return self.bonus[self.status][1]
    def visibleName(self):
        if self.face == FACEUP:
            return '[ACTOR %s] %s'%(self.type, self.name)
        else:
            return '[%s]'%(FACEDOWN)

class DirectorCard(Card):
    def __init__(self, id, name, salary, bonus, ability):
        self.id = id
        self.name = name
        self.salary = salary
        self.bonus = bonus
        self.abilities = ability
        self.cardType = DIRECTORCARD
        self.face = FACEUP
    def getBonus(self, genre):
        return self.bonus[genre]
    def visibleName(self):
        if self.face == FACEUP:
            return '[DIRECTOR] %s'%(self.name)
        else:
            return '[%s]'%(FACEDOWN)

class ScriptCard(Card):
    def __init__(self, id, name, genre, actors, budgetA, budgetB, bonusA, bonusB, instantClassic, instantOscar):
        self.id = id
        self.name = name
        self.genre = genre
        self.actors = actors
        self.budgetA = budgetA
        self.budgetB = budgetB
        self.bonusA = bonusA
        self.bonusB = bonusB
        self.instantClassic = instantClassic
        self.instantOscar = instantOscar
        self.cardType = SCRIPTCARD
        self.face = FACEDOWN
    def visibleName(self):
        if self.face == FACEUP:
            return '[%s] %s (%s)'%(self.genre, self.name, self.actors)
        else:
            return '[%s] %s (?)'%(self.genre, FACEDOWN)

class CrewCard(Card):
    def __init__(self, name):
        self.name = name
        self.type = name
        self.cardType = CREWCARD
        if self.type == ORDINARYCREW:
            self.salary = 0
            self.bonus = 0
        elif self.type == GOODCREW:
            self.salary = 1000
            self.bonus = 1
        elif self.type == EXCELLENTCREW:
            self.salary = 2000
            self.bonus = 2
        self.face = FACEUP
    def visibleName(self):
        if self.face == FACEUP:
            return '[%s]'%(self.name)
        else:
            return '[%s]'%(FACEDOWN)

class WriterCard(Card):
    def __init__(self, name):
        self.name = name
        self.type = name
        self.cardType = WRITERCARD
        self.genre = None
        if self.type == ORDINARYWRITER:
            self.salary = 1000
            self.genre = Dice.genreDie.roll()
        elif self.type == EXCELLENTWRITER:
            self.salary = 2000
        self.face = FACEUP
    def visibleName(self):
        if self.face == FACEUP:
            return '[%s]'%(self.name)
        else:
            return '[%s]'%(FACEDOWN)

class Movie(Card):
    def __init__(self, name):
        self.type = None
        self.name = name
        self.initBonus = 0
        self.currBonus = 0
        self.scriptStack = Deck([])
        self.actorStack = Deck([])
        self.directorStack = Deck([])
        self.crewStack = Deck([])
        self.boxOffice = 0
        self.genre = None
        self.rerun = False
        self.freeReign = False
        self.polished = False
        self.budget = 0
    def getName(self, type=False):
        self.calcBonus()
        if self.scriptStack.countCards > 0:
            return self.scriptStack.cards[0].getName(type) + ' [' + str(self.bonus) + ']'
    def calcBudget(self):
        if self.type == BMOVIE:
            self.budget = self.scriptStack.cards[0].budgetB
        elif self.type == AMOVIE:
            self.budget = self.scriptStack.cards[0].budgetA
    def calcBonus(self):
        if self.rerun == False:
            self.currBonus = self.initBonus
            if self.freeReign == True:
                self.currBonus += 2
            for currScript in self.scriptStack.cards:
                # ABILITIES - BMOVIEPOLISH
                if self.type == 0 and self.polished == False:
                    self.currBonus += currScript.bonusB
                else:
                    self.currBonus += currScript.bonusA
            for currCrew in self.crewStack.cards:
                if currCrew.type == GOODCREW:
                    self.currBonus += 1
                elif currCrew.type == EXCELLENTCREW:
                    self.currBonus += 2
            for currDirector in self.directorStack.cards:
                currGenre = self.scriptStack.cards[0].genre
                self.currBonus += currDirector.bonus[currGenre]
            for currActor in self.actorStack.cards:
                if currActor.status == UNKNOWN:
                    self.currBonus += currActor.bonus[0][1]
                elif currActor.status == STAR:
                    self.currBonus += currActor.bonus[1][1]
        else:
            for currScript in self.scriptStack.cards:
                self.currBonus = self.initBonus + currScript.bonusB
        return
    def calcBoxOffice(self):
        global boxOfficeDie
        self.calcBonus()
        boxOfficeTotal = 0
        for i in range(0, self.bonus):
            boxOfficeTotal += boxOfficeDie[self.type].roll()
        self.boxOffice = boxOfficeTotal
        return self.boxOffice
    def visibleName(self):
        if self.type == AMOVIE: outType = "A"
        else:                   outType = "B"
        self.calcBonus()
        return '[%s] - %s - (%d)'%(outType, self.name, self.currBonus)

class Theater(Card):
    def __init__(self, type=PRIVATE, screens=3, status=OPEN):
        self.name = type
        self.type = type
        self.screens = screens
        self.status = status
        self.movies = Deck([])
        self.movies.maxCards = screens
    def _openTheatre(self):
        if self.status == CLOSED:
            self.status == OPEN
            return True
        else:
            return False
    def _closeTheatre(self):
        if self.status == OPEN:
            self.status == CLOSED
            return True
        else:
            return False
    def _liquidateTheatre(self):
        if self.status == OPEN:
            self.status == CLOSED
            return True
        else:
            return False
    def bookMovie(self, movieStack):
        if self.movies.countCards() < self.screens:
            self.movies.addCards(movieStack)
            print self.movies.cards
            return True
        else:
            return False
