import csv, curses, prettytable

import Game
from Constants import *

global stdscr, statusWindow, scriptWindow, employWindow, officeWindow, logWindow, menuWindow, gameStatusWindow
global csvOutput, logOutput

def initOutput():
    global stdscr, statusWindow, scriptWindow, employWindow, officeWindow, logWindow, menuWindow, gameStatusWindow
    global csvOutput, logOutput
    stdscr = curses.initscr()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    #curses.echo()
    stdscr.addstr('Please resize your window to 220 x 90\n')
    stdscr.addstr('Press any key when done...')
    c = stdscr.getch()
    statusWindow = curses.newwin(20, 220, 3, 0)
    statusWindow.scrollok(True)
    gameStatusWindow = curses.newwin(3, 220, 0, 0)
    scriptWindow = curses.newwin(10, 90, 23, 0)
    employWindow = curses.newwin(15, 50, 23, 90)
    employWindow.scrollok(True)
    officeWindow = curses.newwin(25, 140, 33, 0)
    logWindow = curses.newwin(45, 80, 23, 140)
    logWindow.scrollok(True)
    menuWindow = curses.newwin(20, 110, 48, 0)
    menuWindow.scrollok(True)

    csvOutput = csv.writer(open("output.csv", "wb"))
    csvOutput.writerow(['Game', 'Year', 'Trimester', 'Studio', 'Cash', 'Prestige', 'Theaters', 'Directors', 'Actors', 'Scripts', 'Writers', 'Crew', 'Statuettes', 'Oscars', 'Classics', 'NoMovies', 'BoxOfficeEarnings'])
    logOutput = open("log.txt", "w")

def csvoutput():
    csvOutput
    for currPlayer in Game.board.players:
        #outGame         = Game.board.currGame
        outYear         = Game.board.currYear
        outTrimester    = ((Game.board.currYear-1) * 3) + Game.board.currTrimester
        outStudio       = currPlayer.studio
        outCash         = currPlayer.money
        outPrestige     = currPlayer.prestige
        outTheaters     = currPlayer.theaterStack.countCards()
        outDirectors    = currPlayer.directorStack.countCards()
        outActors       = currPlayer.actorStack.countCards()
        outScripts      = currPlayer.scriptStack.countCards()
        outWriters      = currPlayer.writerStack.countCards()
        outCrew         = currPlayer.crewStack.countCards()
        outStatuettes   = currPlayer.statuettes
        outOscars       = currPlayer.oscars
        outClassics     = currPlayer.archiveStack.countCards()
        outNoMovies     = currPlayer.noMoviesProduced
        outBoxOffice    = currPlayer.boxOfficeEarnings
        #csvOutput.writerow([outGame, outYear, outTrimester, outStudio, outCash,outPrestige, outTheaters, outDirectors, outActors, outScripts, outWriters, outCrew, outStatuettes, outOscars, outClassics, outNoMovies, outBoxOffice])
        csvOutput.writerow([outYear, outTrimester, outStudio, outCash,outPrestige, outTheaters, outDirectors, outActors, outScripts, outWriters, outCrew, outStatuettes, outOscars, outClassics, outNoMovies, outBoxOffice])

def killOutput():
    global logOutput
    logOutput.close()
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()

def printToWindow(text, window, x=None, y=None, colorPair=0):
    if x and y:
        window.addstr(x, y, text, curses.color_pair(colorPair)); window.refresh()
    else:
        window.addstr(text, curses.color_pair(colorPair)); window.refresh()

def printToLog(text=""):
    global logOutput
    printToWindow(text+'\n', logWindow)
    logOutput.write(text)

def updateScreen():
    printPlayerStatus()
    printScriptStatus()
    printEmploymentStatus()
    printProductionStatus()
    printGameStatus()

def printPlayerStatus():
    statusTable = prettytable.PrettyTable(['Player', 'Studio', 'Cash', 'Pres', 'Thtrs', 'Dirs', 'Acts', 'Scripts', 'Writers', 'Crew', 'Stats', 'Oscars'])
    directorStack = ""
    actorStack = ""
    scriptStack = ""
    writerStack = ""
    crewStack = ""
    for i in Game.board.powerTrack:
        for j in Game.board.players[i].directorStack.cards:
            directorStack += j.visibleName() + '\n'
        for j in Game.board.players[i].actorStack.cards:
            actorStack += j.visibleName() + '\n'
        for j in Game.board.players[i].scriptStack.cards:
            scriptStack += j.visibleName() + '\n'
        for j in Game.board.players[i].writerStack.cards:
            writerStack += j.visibleName() + '\n'
        for j in Game.board.players[i].crewStack.cards:
            crewStack += j.visibleName() + '\n'
        statusTable.add_row([Game.board.players[i].name, Game.board.players[i].studio, Game.board.players[i].money, Game.board.players[i].prestige, Game.board.players[i].theaterStack.countCards(), directorStack, actorStack, scriptStack, writerStack, crewStack, Game.board.players[i].statuettes, Game.board.players[i].oscars])
    statusWindow.clear()
    printToWindow(str(statusTable), statusWindow, 0, 0)
    statusWindow.refresh()
def printScriptStatus():
    statusTable = prettytable.PrettyTable(['Genre', 'Number', 'Names'])
    for currGenre in GENRES:
        currTopCard = Game.board.scriptDecks.get(currGenre).cards[0]
        if currTopCard != None:
            statusTable.add_row([currGenre, Game.board.scriptDecks.get(currGenre).countCards(), currTopCard.visibleName()])
        else:
            statusTable.add_row([currGenre, Game.board.scriptDecks(currGenre).countCards(), 'EMPTY'])
    scriptWindow.clear()
    printToWindow(str(statusTable), scriptWindow, 0, 0)
    scriptWindow.refresh()
def printEmploymentStatus():
    statusTable = prettytable.PrettyTable()
    employmentStack = ""
    for j in Game.board.employmentOffice.cards:
        employmentStack += j.visibleName() + '\n'
    statusTable.add_column("Employment Office [%d/%d]"%(Game.board.employmentOffice.countCards(), len(Game.board.players) + 1), [employmentStack])
    employWindow.clear()
    printToWindow(str(statusTable), employWindow, 0, 0)
    employWindow.refresh()
def printProductionStatus():
    statusTable = prettytable.PrettyTable(['Player', 'A Prod', 'B Prod', 'A Box', 'B Box', 'Archive'])
    productionStack = ["", ""]
    boxOfficeStack =["", ""]
    archiveStack = ""
    for i in Game.board.powerTrack:
        for type in [0,1]:
            for j in Game.board.players[i].productionStack[type].cards:
                productionStack[type] += j.visibleName() + '\n'
            for j in Game.board.players[i].boxOfficeStack[type].cards:
                boxOfficeStack[type] += j.visibleName() + '\n'
        for j in Game.board.players[i].archiveStack.cards:
            archiveStack[type] += j.visibleName() + '\n'
        statusTable.add_row([Game.board.players[i].name, productionStack[1], productionStack[0], boxOfficeStack[1], boxOfficeStack[0], archiveStack])

    officeWindow.clear()
    printToWindow(str(statusTable), officeWindow, 0, 0)
    officeWindow.refresh()
def printGameStatus():
    gameStatusWindow.clear()
    printToWindow('\tYEAR: %d'%(Game.board.currYear) + '\t\tTRIMESTER: %d'%(Game.board.currTrimester) + '\tPublic Theater: %s'%(str(Game.board.theaterStack.cards[0].screens - Game.board.theaterStack.cards[0].movies.countCards())), gameStatusWindow, 1, 1)
    #printToWindow('\tYEAR: %d'%(currYear) + '\t\tTRIMESTER: %d'%(currTrimester) + '\tPublic Theater: %s'%(str(len([i for i in theaters[0].screens if i == None]))), gameStatusWindow, 1, 1)
    gameStatusWindow.refresh()
