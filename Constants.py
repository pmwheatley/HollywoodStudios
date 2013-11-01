GAMESEED = 4184

""" Turn Status """
EMPLOYEESPAID = 'EMPLOYEESPAID'
UPKEEPPAID = 'UPKEEPPAID'
THEATERBOUGHT = 'THEATERBOUGHT'
SCRIPTSCLAIMED = 'SCRIPTSCLAIMED'

""" Theater Costs """
THEATERCOST	= 20000
THEATERUPKEEP	= 4000
THEATERREOPEN	= 2000
THEATERSALE	= 5000

SCRIPTCOST	= 1000

AMOVIE = 1
BMOVIE = 0

""" Theater Status """
PUBLIC		= 0
PRIVATE		= 1
OPEN		= 0
CLOSED		= 1

""" Studios """
MGM	= 'MGM'
PAR	= 'PARAMOUNT'
FOX	= 'FOX'
UNI	= 'UNIVERSAL'
WAR	= 'WARNER BROS'
STUDIOS	= [MGM, PAR, FOX, UNI, WAR]

""" Card Types """
ACTORCARD	= 'ACTOR'
DIRECTORCARD	= 'DIRECTOR'
SCRIPTCARD	= 'SCRIPT'
CREWCARD	= 'CREW'
WRITERCARD	= 'WRITER'

""" Craftsmen """
ORDINARYCREW	= 'ORDINARY CREW'
GOODCREW	= 'GOOD CREW'
EXCELLENTCREW	= 'EXCELLENT CREW'
ORDINARYWRITER	= 'ORDINARY WRITER'
EXCELLENTWRITER	= 'EXCELLENT WRITER'

""" Card Faces """
FACEUP		= 0
FACEDOWN	= 'FACEDOWN'

""" Actor Status """
UNKNOWN		= 0
STAR		= 1

""" Actor Types """
BD	= 'BD'
DM	= 'DM'
C	= 'C'
FH	= 'FH'
S	= 'S'
SW	= 'SW'
QL	= 'QL'
TYPES	= [BD, DM, C, FH, S, SW, QL]

""" Genres """
FILMNOIR	= 'FILMNOIR'
ROMANCE		= 'ROMANCE'
HORROR		= 'HORROR'
COMEDY		= 'COMEDY'
EPIC		= 'EPIC'
SWORDS		= 'SWORDS'
GENRES		= [FILMNOIR, ROMANCE, HORROR, COMEDY, EPIC, SWORDS]

""" Box Office Dice """
ADICE	= [2000, 4000, 6000, 8000, 10000, 12000]
BDICE	= [1000, 2000, 3000, 4000, 5000, 6000]

""" Abilities """
ALLMOVIEBONUS	      	= 0    # Studios + Directors
AMOVIEBONUS             = 1    # Studios + Directors
BMOVIEBONUS             = 2    # Studios + Directors
AMOVIEEXTRACOST         = 3    # Studios + Directors
BMOVIEEXTRACOST         = 4    # Studios + Directors
AMOVIEFIRSTSTAR         = 5
BMOVIEFIRSTSTAR         = 6
AMOVIESONLY             = 7    # Studios
BMOVIESONLY             = 8    # Studios
BMOVIEPOLISH            = 9    # Studios
STARLIMIT               = 10
BLOCKBOOKING            = 11   # Studios
FREEPUBLICBOOK          = 12   # Studios
MULTIACTIONS            = 13
BOGENREREROLL           = 14
MUSTFREEREIGN           = 15   # Studios
CANTFREEREIGN           = 16   # Studios
ALSOWRITER              = 17   # Directors
ROLLOSCAR               = 18   # Studios + Directors
FILMNOIRROLLCLASSIC     = 19   # Studios + Directors
ROMANCEROLLCLASSIC      = 20   # Studios + Directors
HORRORROLLCLASSIC       = 21   # Studios + Directors
COMEDYROLLCLASSIC       = 22   # Studios + Directors
EPICROLLCLASSIC         = 23   # Studios + Directors
SWORDSROLLCLASSIC       = 24   # Studios + Directors
FILMNOIRBONUS           = 25   # Studios + Directors
ROMANCEBONUS            = 26   # Studios + Directors
HORRORBONUS             = 27   # Studios + Directors
COMEDYBONUS             = 28   # Studios + Directors
EPICBONUS               = 29   # Studios + Directors
SWORDSBONUS             = 30   # Studios + Directors

""" Actions """
ACTPAYSALARIES	= 'Pay Employee Salaries'
ACTFIREEMPLOY	= 'Fire an Employee'
ACTPAYUPKEEP	= 'Pay Theater Upkeep'
ACTOPENTHEATER	= 'Reopen a Theater'
ACTCLOSETHEATER	= 'Close a Theater'
ACTSELLTHEATER	= 'Sell a Theater'
ACTCLAIMSCRIPTS = 'Claim Scripts From Writers'
UPKPHASEACTIONS	= [ACTCLAIMSCRIPTS, ACTPAYSALARIES, ACTFIREEMPLOY, ACTPAYUPKEEP, ACTOPENTHEATER, ACTCLOSETHEATER, ACTSELLTHEATER]

ACTBUYSCRIPT	= 'Buy a script'
ACTDRAWACTOR	= 'Draw an Actor Card'
ACTDRAWCRAFT	= 'Draw a Craftsmen Card'
ACTHIREOFFICE	= 'Hire from the Office'
ACTPUBLICBOOK	= 'Book at the Public Theater'
ACTPHASEACTIONS	= [ACTBUYSCRIPT, ACTDRAWACTOR, ACTDRAWCRAFT, ACTHIREOFFICE, ACTPUBLICBOOK]

ACTBUILDTHEATER	= 'Build a Theater'
CONPHASEACTIONS = [ACTBUILDTHEATER]

ACTPRIVATEBOOK	= 'Book at a Private Theater'
PVTPHASEACTIONS	= [ACTPRIVATEBOOK]

ACTUSEABILITY	= 'Use an ability'
ACTPLAYEVENT	= 'Play an Event card'
ANYPHASEACTIONS	= [ACTUSEABILITY, ACTPLAYEVENT]

ACTPHASESKIP	= 'Skip to next phase'

ACTTRADE2STAT   = 'Trade 2 Golden Statuettes'
ACTTRADE1STAT   = 'Trade 1 Golden Statuette'
ACTFREEACTIONS  = [ACTTRADE2STAT, ACTTRADE1STAT]


""" Choice Menus """
YES		= 'Yes'
NO		= 'No'
MENUYESNO	= [YES, NO]
