import csv, curses

import Game

global stdscr, statusWindow, scriptWindow, employWindow, officeWindow, logWindow, menuWindow, gameStatusWindow
global csvOutput, logOutput

def initOutput():
    global stdscr, statusWindow, scriptWindow, employWindow, officeWindow, logWindow, menuWindow, gameStatusWindow
    global csvOutput, logOutput
    stdscr = curses.initscr()
    curses.echo()
    stdscr.addstr('Please resize your window to 220 x 90\n')
    stdscr.addstr('Press any key when done...')
    c = stdscr.getch()
    statusWindow = curses.newwin(40, 220, 3, 0)
    statusWindow.scrollok(True)
    gameStatusWindow = curses.newwin(3, 220, 0, 0)
    scriptWindow = curses.newwin(10, 90, 43, 0)
    employWindow = curses.newwin(15, 50, 43, 90)
    employWindow.scrollok(True)
    officeWindow = curses.newwin(25, 140, 53, 0)
    logWindow = curses.newwin(45, 80, 43, 140)
    logWindow.scrollok(True)
    menuWindow = curses.newwin(10, 110, 78, 0)
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

def printToWindow(text, window, x=None, y=None):
    if x and y:
        window.addstr(x, y, text); window.refresh()
    else:
        window.addstr(text); window.refresh()
def printToLog(text=""):
    global logOutput
    printToWindow(text, logWindow)
    logOutput.write(text)
