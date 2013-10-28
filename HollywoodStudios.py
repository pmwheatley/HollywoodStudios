""" Hollywood Studios v0.3 """

import Cards, Players, CardData, Dice, Game, Output
from Constants import *

Output.initOutput()

Player1 = Players.Player("Phil")
Player1.studio = MGM

Game.board = Game.Board([Player1])

for i in [1,2,3]:

    Output.updateScreen()

    Player1.doUpkeepPhase()
    Player1.doConstructionPhase()
    Player1.doActionPhase()

for i in Game.board.theaterStack.cards[0].movies:
    Output.printToWindow(menuWindow, i.name)

Output.killOutput()

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
