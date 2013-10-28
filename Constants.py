GAMESEED = 4184

""" Turn Status """
EMPLOYEESPAID = None
UPKEEPPAID = None

""" Theater Costs """
THEATERCOST	= 20000
THEATERUPKEEP	= 4000
THEATERREOPEN	= 2000
THEATERSALE	= 5000

SCRIPTCOST	= 1000

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
ALLMOVIEBONUS		= 0
AMOVIEBONUS             = 1
BMOVIEBONUS             = 2
AMOVIEEXTRACOST         = 3
BMOVIEEXTRACOST         = 4
AMOVIEFIRSTSTAR         = 5
BMOVIEFIRSTSTAR         = 6
AMOVIESONLY             = 7
BMOVIESONLY             = 8
BMOVIEPOLISH            = 9
STARLIMIT               = 10
BLOCKBOOKING            = 11
FREEPUBLICBOOK          = 12
MULTIACTIONS            = 13
BOGENREREROLL           = 14
MUSTFREEREIGN           = 15
CANTFREEREIGN           = 16
ALSOWRITER              = 17
ROLLOSCAR               = 18
FILMNOIRROLLCLASSIC     = 19
ROMANCEROLLCLASSIC      = 20
HORRORROLLCLASSIC       = 21
COMEDYROLLCLASSIC       = 22
EPICROLLCLASSIC         = 23
SWORDSROLLCLASSIC       = 24
FILMNOIRBONUS           = 25
ROMANCEBONUS            = 26
HORRORBONUS             = 27
COMEDYBONUS             = 28
EPICBONUS               = 29
SWORDSBONUS             = 30

""" Actions """
ACTPAYSALARIES	= 'Pay Employee Salaries'
ACTFIREEMPLOY	= 'Fire an Employee'
ACTPAYUPKEEP	= 'Pay Theater Upkeep'
ACTOPENTHEATER	= 'Reopen a Theater'
ACTCLOSETHEATER	= 'Close a Theater'
ACTSELLTHEATER	= 'Sell a Theater'
UPKPHASEACTIONS	= [ACTPAYSALARIES, ACTFIREEMPLOY, ACTPAYUPKEEP, ACTOPENTHEATER, ACTCLOSETHEATER, ACTSELLTHEATER]

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

""" Choice Menus """
YES		= 'Yes'
NO		= 'No'
MENUYESNO	= [YES, NO]
