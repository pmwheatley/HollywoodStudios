import copy

import Cards, CardData
from Constants import *

class Board():
    def __init__(self, players=[]):
        self.players = players
        self.currYear = 1
        self.currTrimester = 1
        self.powerTrack = [0]

        """ Initiate Decks """
        self.actorsDeck = copy.deepcopy(CardData.ACTORSDECK)
        self.scriptDecks = {FILMNOIR: copy.deepcopy(CardData.FILMNOIRDECK), ROMANCE: copy.deepcopy(CardData.ROMANCEDECK), HORROR: copy.deepcopy(CardData.HORRORDECK), COMEDY: copy.deepcopy(CardData.COMEDYDECK), EPIC: copy.deepcopy(CardData.EPICDECK), SWORDS: copy.deepcopy(CardData.SWORDSDECK)}

        self.tmpDirectorsDeck = copy.deepcopy(CardData.DIRECTORSDECK)
        self.tmpWritersDeck  = copy.deepcopy(CardData.WRITERSDECK)
        self.tmpCrewDeck = copy.deepcopy(CardData.CREWDECK)
        self._distributeCards()
        self.craftsDeck = Cards.Deck(self.tmpDirectorsDeck.cards + self.tmpWritersDeck.cards + self.tmpCrewDeck.cards)

        self.employmentOffice = Cards.Deck([])

        """ Initiate Theater """
        self.theaterStack = Cards.Deck([Cards.Theater(type=PUBLIC, screens=len(self.players)+1, status=OPEN)])

        #self._shuffleAll()
    def _shuffleAll(self):
        self.actorsDeck.shuffle()
        self.scriptDecks['FILMNOIR'].shuffle()
        self.scriptDecks['ROMANCE'].shuffle()
        self.scriptDecks['HORROR'].shuffle()
        self.scriptDecks['COMEDY'].shuffle()
        self.scriptDecks['EPIC'].shuffle()
        self.scriptDecks['SWORDS'].shuffle()
        self.craftsDeck.shuffle()
    def _distributeCards(self):
        for currPlayer in self.players:
            if currPlayer.studio == MGM:
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=68))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=16))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=50))
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=20))
                currPlayer.crewStack.addCards(self.tmpCrewDeck.drawCards(names=ORDINARYCREW))
                currPlayer.writerStack.addCards(self.tmpWritersDeck.drawCards(names=EXCELLENTWRITER))
            elif currPlayer.studio == PAR:
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=25))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=68))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=3))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=23))
                currPlayer.crewStack.addCards(self.tmpCrewDeck.drawCards(names=ORDINARYCREW))
                currPlayer.writerStack.addCards(self.tmpWritersDeck.drawCards(names=ORDINARYWRITER))
            elif currPlayer.studio == FOX:
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=28))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=56))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=32))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=46))
                currPlayer.crewStack.addCards(self.tmpCrewDeck.drawCards(names=ORDINARYCREW))
                currPlayer.writerStack.addCards(self.tmpWritersDeck.drawCards(names=ORDINARYWRITER))
            elif currPlayer.studio == UNI:
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=16))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=29))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=2))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=19))
                currPlayer.crewStack.addCards(self.tmpCrewDeck.drawCards(names=ORDINARYCREW))
                currPlayer.writerStack.addCards(self.tmpWritersDeck.drawCards(names=ORDINARYWRITER))
            elif currPlayer.studio == WAR:
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=13))
                currPlayer.directorStack.addCards(self.tmpDirectorsDeck.drawCards(ids=23))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=21))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=53))
                currPlayer.actorStack.addCards(self.actorsDeck.drawCards(ids=39))
                currPlayer.crewStack.addCards(self.tmpCrewDeck.drawCards(names=ORDINARYCREW))

    def revealScripts(self):
        for currGenre in GENRES:
            self.scriptDecks[currGenre].cards[0].face = FACEUP

global board
board = Board()
