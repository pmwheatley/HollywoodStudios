""" Hollywood Studios v0.3 """

import Cards, Players, CardData, Dice, Game
from Constants import *

Player1 = Players.Player("Phil")
Player1.studio = MGM

Game.board = Game.Board([Player1])

for i in [1,2,3]:

    Player1.doUpkeepPhase()
    Player1.doConstructionPhase()
    Player1.doActionPhase()

for i in Game.board.theaterStack.cards[0].movies:
    print i.name

""" SETUP PHASE """

""" YEAR 1 """

"""     TRIM 1 """
"""     UPKEEP PHASE """
"""     SCRIPTS PHASE """
"""     EMPLOYMENT PHASE """

"""         PLAYER 1 """
"""         CONSTRUCTION PHASE """
"""         ACTION PHASE """
"""         PRIVATE BOOKING PHASE """

""" BOX OFFICE PHASE """

""" FINAL PRESTIGE PHASE """
