from Cards import *
from Constants import *

ACTORSDECK	= Deck([	ActorCard(0,	'Charlie Chaplin',	C,	[3000, 6000],	[[0, 0],	[4, 4]]),
				ActorCard(1,	'Buster Keaton',	C,	[2000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(2,	'Mack Sennett',		C,	[3000, 4000],	[[0, 0],	[2, 1]]),
				ActorCard(3,	'Marx Brothers',	C,	[2000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(4,	'Laurel & Hardy',	C,	[2000, 5000],	[[0, 0],	[2, 3]]),
				ActorCard(5,	'Harold Lloyd',		C,	[1000, 3000],	[[0, 0],	[1, 1]]),
				ActorCard(6,	'Will Rogers',		C,	[1000, 3000],	[[0, 0],	[1, 2]]),
				ActorCard(7,	'Karl Dane',		C,	[1000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(8,	'Boris Karloff',	C,	[2000, 5000],	[[0, 0],	[2, 4]]),
				ActorCard(9,	'Bela Lugosi',		C,	[2000, 5000],	[[0, -1],	[4, 1]]),
				ActorCard(11,	'Gene Kelly',		BD,	[2000, 4000],	[[0, 0],	[1, 3]]),
				ActorCard(11,	'Fred Astaire',		BD,	[2000, 5000],	[[0, 0],	[3, 4]]),
				ActorCard(12,	'Rex Harrison',		BD,	[1000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(13,	'Colin Clive',		BD,	[1000, 3000],	[[0, -1],	[2, 0]]),
				ActorCard(14,	'Tyrone Power',		BD,	[1000, 3000],	[[0, 0],	[1, 1]]),
				ActorCard(15,	'John Gilbert',		BD,	[3000, 5000],	[[0, -1],	[3, 1]]),
				ActorCard(16,	'Rudolph Valentino',	BD,	[3000, 5000],	[[0, -1],	[3, 0]]),
				ActorCard(17,	'Cary Grant',		BD,	[3000, 6000],	[[0, 0],	[4, 4]]),
				ActorCard(18,	'Milton Sills',		BD,	[1000, 3000],	[[0, -1],	[1, 0]]),
				ActorCard(19,	'James Stewart',	BD,	[2000, 5000],	[[0, 0],	[3, 3]]),
				ActorCard(20,	'Humphrey Bogart',	DM,	[3000, 6000],	[[0, 0],	[3, 5]]),
				ActorCard(21,	'James Cagney',		DM,	[2000, 5000],	[[0, 0],	[3, 4]]),
				ActorCard(22,	'Edward G. Robinson',	DM,	[1000, 3000],	[[0, -1],	[1, 0]]),
				ActorCard(23,	'Gary Cooper',		DM,	[2000, 4000],	[[0, 0],	[2, 1]]),
				ActorCard(24,	'Charles Laughton',	DM,	[3000, 5000],	[[0, 0],	[3, 3]]),
				ActorCard(25,	'Peter Lorre',		DM,	[1000, 4000],	[[0, 0],	[2, 2]]),
				ActorCard(26,	'Charles Boyer',	DM,	[3000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(27,	'Sterling Hayden',	DM,	[2000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(28,	'Fred MacMurray',	DM,	[1000, 3000],	[[0, -1],	[2, 0]]),
				ActorCard(29,	'Lon Chaney',		DM,	[2000, 5000],	[[0, -1],	[4, 1]]),
				ActorCard(30,	'Charlton Heston',	FH,	[3000, 5000],	[[0, 0],	[2, 4]]),
				ActorCard(31,	'John Gielgud',		FH,	[1000, 3000],	[[0, 0],	[1, 1]]),
				ActorCard(32,	'Henry Fonda',		FH,	[1000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(33,	'Spencer Tracy',	FH,	[1000, 3000],	[[0, -1],	[1, 1]]),
				ActorCard(34,	'Errol Flynn',		FH,	[2000, 5000],	[[0, -1],	[4, 0]]),
				ActorCard(35,	'Tom Mix',		FH,	[2000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(36,	'Douglas Fairbanks',	FH,	[3000, 6000],	[[0, -1],	[5, 2]]),
				ActorCard(37,	'Laurence Olivier',	FH,	[2000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(38,	'William S. Hart',	FH,	[1000, 3000],	[[0, 0],	[1, 0]]),
				ActorCard(39,	'John Barrymore',	FH,	[3000, 5000],	[[0, 0],	[3, 3]]),
				ActorCard(40,	'Mary Pickford',	S,	[3000, 6000],	[[0, -1],	[5, 2]]),
				ActorCard(41,	'Alice Faye',		S,	[2000, 4000],	[[0, 0],	[2, 1]]),
				ActorCard(42,	'Ava Gardner',		S,	[3000, 5000],	[[0, -1],	[3, 3]]),
				ActorCard(43,	'Judy Garland',		S,	[3000, 5000],	[[0, 0],	[2, 4]]),
				ActorCard(44,	'Shirley Temple',	S,	[1000, 5000],	[[0, 0],	[4, 1]]),
				ActorCard(45,	'Lillian Gish',		S,	[2000, 3000],	[[0, 0],	[1, 1]]),
				ActorCard(46,	'Janet Gaynor',		S,	[2000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(47,	'Ginger Rogers',	S,	[2000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(48,	'Claudette Colbert',	S,	[1000, 3000],	[[0, 0],	[1, 2]]),
				ActorCard(49,	'Jeanette MacDonald',	S,	[1000, 3000],	[[0, -1],	[1, 0]]),
				ActorCard(50,	'Mae West',		SW,	[3000, 5000],	[[0, -1],	[3, 1]]),
				ActorCard(51,	'Marlene Dietrich',	SW,	[3000, 5000],	[[0, 0],	[3, 2]]),
				ActorCard(52,	'Carole Lombard',	SW,	[2000, 5000],	[[0, 0],	[4, 1]]),
				ActorCard(53,	'Bette Davis',		SW,	[2000, 4000],	[[0, 0],	[2, 3]]),
				ActorCard(54,	'Jean Harlow',		SW,	[3000, 6000],	[[0, 0],	[3, 5]]),
				ActorCard(55,	'Rita Hayworth',	SW,	[2000, 4000],	[[0, 0],	[2, 2]]),
				ActorCard(56,	'Theda Bara',		SW,	[2000, 4000],	[[0, -1],	[2, 0]]),
				ActorCard(57,	'Mary Astor',		SW,	[1000, 3000],	[[0, -1],	[1, 2]]),
				ActorCard(58,	'Nita Naldi',		SW,	[1000, 3000],	[[0, -1],	[1, 0]]),
				ActorCard(59,	'Barbara Stanwyck',	SW,	[1000, 3000],	[[0, 0],	[1, 1]]),
				ActorCard(60,	'Greta Garbo',		QL,	[3000, 6000],	[[1, 0],	[5, 2]]),
				ActorCard(61,	'Ingrid Bergman',	QL,	[3000, 6000],	[[1, 1],	[4, 4]]),
				ActorCard(62,	'Mabel Normand',	QL,	[2000, 4000],	[[1, 0],	[2, 0]]),
				ActorCard(63,	'Irene Dunne',		QL,	[2000, 4000],	[[1, 0],	[2, 1]]),
				ActorCard(64,	'Joan Crawford',	QL,	[2000, 4000],	[[1, 1],	[2, 3]]),
				ActorCard(65,	'Vivien Leigh',		QL,	[3000, 5000],	[[1, 1],	[2, 4]]),
				ActorCard(66,	'Katherine Hepburn',	QL,	[3000, 6000],	[[1, 1],	[4, 4]]),
				ActorCard(67,	'Norma Shearer',	QL,	[3000, 5000],	[[1, 0],	[3, 1]]),
				ActorCard(68,	'Gloria Swanson',	QL,	[3000, 5000],	[[1, 1],	[3, 0]]),
				ActorCard(69,	'Lauren Bacall',	QL,	[3000, 6000],	[[1, 1],	[4, 5]])])
DIRECTORSDECK	= Deck([	DirectorCard(0,		'Allan Smithee',	1000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(1,		'Georges Cochrane',	1000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(2,		'Beaumont Smith',	1000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 1},	{}),
				DirectorCard(3,		'Cecil M. Hepworth',	1000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(4,		'Sinclair Hill',	1000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 1,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(5,		'Harry Edwards',	1000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 0,	COMEDY: 1,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(6,		'Raoul Walsh',		2000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 1},	{}),
				DirectorCard(7,		'Frank Wilson',		2000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 1,	SWORDS: 0},	{}),
				DirectorCard(8,		'John K. Wells',	2000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 1,	COMEDY: 0,	EPIC: 0,	SWORDS: 1},	{}),
				DirectorCard(9,		'Joseph Henabery',	2000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 1,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(10,	'Edgar Lewis',		2000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 1,	COMEDY: 1,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(11,	'Clarence Brown',	2000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 0,	EPIC: 1,	SWORDS: 0},	{}),
				DirectorCard(12,	'Franklyn Barrett',	2000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 1,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(13,	'Busby Berkeley',	3000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 1,	COMEDY: 1,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(14,	'D.W. Griffith',	3000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 1,	SWORDS: 1},	{}),
				DirectorCard(15,	'Rouben Mamoulian',	3000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 1,	COMEDY: 1,	EPIC: 0,	SWORDS: 0},	{}),
				DirectorCard(16,	'Erich Von Stroheim',	3000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 3,	SWORDS: 0},	{}),
				DirectorCard(17,	'Tod Browning',		3000,	{FILMNOIR: 0,	ROMANCE: 0,	HORROR: 0,	COMEDY: 1,	EPIC: 0,	SWORDS: 2},	{}),
				DirectorCard(18,	'Edgar Jones',		3000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 1},	{}),
				DirectorCard(19,	'King Vidor',		4000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 1,	COMEDY: 0,	EPIC: 1,	SWORDS: 1},	{}),
				DirectorCard(20,	'F.W. Murneau',		4000,	{FILMNOIR: 1,	ROMANCE: 1,	HORROR: 1,	COMEDY: 0,	EPIC: 1,	SWORDS: 0},	{}),
				DirectorCard(21,	'Elia Kazan',		4000,	{FILMNOIR: 1,	ROMANCE: 1,	HORROR: 0,	COMEDY: 0,	EPIC: 1,	SWORDS: 1},	{}),
				DirectorCard(22,	'Leslie Goodwins',	4000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 1,	EPIC: 0,	SWORDS: 1},	{BMOVIEBONUS: 1}),
				DirectorCard(23,	'Ernst Lubitsch',	4000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 2,	EPIC: 0,	SWORDS: 0},	{ALSOWRITER: True}),
				DirectorCard(24,	'Alfred Hitchcock',	4000,	{FILMNOIR: 2,	ROMANCE: 0,	HORROR: 2,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{AMOVIEEXTRACOST: -2000}),
				DirectorCard(25,	'Cecil B. DeMille',	5000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 0,	EPIC: 3,	SWORDS: 0},	{AMOVIEBONUS: 1}),
				DirectorCard(26,	'Frank Capra',		5000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 2,	EPIC: 1,	SWORDS: 0},	{ROLLOSCAR: 2}),
				DirectorCard(27,	'James Whale',		5000,	{FILMNOIR: 1,	ROMANCE: 0,	HORROR: 3,	COMEDY: 0,	EPIC: 0,	SWORDS: 0},	{FILMNOIRROLLCLASSIC: 2,	HORRORROLLCLASSIC: 2}),
				DirectorCard(28,	'John Ford',		5000,	{FILMNOIR: 0,	ROMANCE: 1,	HORROR: 0,	COMEDY: 0,	EPIC: 0,	SWORDS: 3},	{BMOVIEBONUS: 1}),
				DirectorCard(29,	'Victor Fleming',	5000,	{FILMNOIR: 2,	ROMANCE: 0,	HORROR: 1,	COMEDY: 2,	EPIC: 0,	SWORDS: 1},	{AMOVIEEXTRACOST: 1000,	BMOVIEEXTRACOST:1000})])

FILMNOIRDECK	= Deck([ScriptCard(0,	'The Big Sleep',				FILMNOIR,	[DM, SW, C],	4000,	1000,	2,	0,	False,	False),
						ScriptCard(1,	'Rififi',						FILMNOIR,	[BD, DM],		4000,	1000,	2,	0,	False,	False),
						ScriptCard(2,	'The Asphalt Jungle',			FILMNOIR,	[DM, S],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(3,	'Touch of Evil',				FILMNOIR,	[BD, DM],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(4,	'The Killing',					FILMNOIR,	[DM, C],		6000,	3000,	3,	1,	False,	False),
						ScriptCard(5,	'The Third Man',				FILMNOIR,	[DM, SW],		5000,	1000,	3,	0,	False,	False),
						ScriptCard(6,	'Double Indemnity',				FILMNOIR,	[DM, SW],		5000,	2000,	3,	1,	False,	True),
						ScriptCard(7,	'Sunset Boulevard',				FILMNOIR,	[BD, SW, S],	7000,	4000,	4,	2,	True,	False),
						ScriptCard(8,	'Strangers on a Train',			FILMNOIR,	[BD, C],		4000,	1000,	2,	0,	False,	False),
						ScriptCard(9,	'Casablanca',					FILMNOIR,	[DM, BD, S],	7000,	4000,	5,	2,	True,	True),
						ScriptCard(10,	'Scarface',						FILMNOIR,	[DM, SW],		5000,	2000,	2,	0,	False,	True),
						ScriptCard(11,	'The Maltese Falcon',			FILMNOIR,	[DM, SW, DM],	6000,	3000,	4,	2,	True,	False),
						ScriptCard(12,	'The Blue Angel',				FILMNOIR,	[SW, DM],		6000,	3000,	4,	2,	False,	False),
						ScriptCard(13,	'Notorious',					FILMNOIR,	[DM, SW],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(14,	'The Public Enemy',				FILMNOIR,	[DM],			5000,	2000,	3,	1,	False,	False),
						ScriptCard(15,	'Key Largo',					FILMNOIR,	[BD, SW, DM],	5000,	2000,	3,	1,	False,	False)])
ROMANCEDECK	= Deck([	ScriptCard(16,	'Golden Earrings',				ROMANCE,	[SW, BD],		6000,	2000,	3,	0,	False,	False),
						ScriptCard(17,	'Romeo and Juliet',				ROMANCE,	[S, BD],		7000,	3000,	4,	2,	False,	False),
						ScriptCard(18,	'The Love Trap',				ROMANCE,	[S, FH],		5000,	3000,	2,	2,	False,	False),
						ScriptCard(19,	"It's a Wonderful Life",		ROMANCE,	[BD, C, S],		9000,	5000,	4,	2,	True,	False),
						ScriptCard(20,	'Now, Voyager',					ROMANCE,	[SW, FH],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(21,	"Heart o' the Hills",			ROMANCE,	[QL, BD],		4000,	2000,	2,	1,	False,	False),
						ScriptCard(22,	'My Best Girl',					ROMANCE,	[BD, QL],		6000,	3000,	3,	2,	False,	False),
						ScriptCard(23,	'Grand Hotel',					ROMANCE,	[SW, BD, S],	7000,	3000,	4,	2,	True,	False),
						ScriptCard(24,	'Ninotchka',					ROMANCE,	[QL, BD],		5000,	2000,	3,	1,	True,	False),
						ScriptCard(25,	'Small Town Girl',				ROMANCE,	[S, C],			4000,	1000,	2,	0,	False,	False),
						ScriptCard(26,	'The Eagle',					ROMANCE,	[BD, SW],		4000,	2000,	2,	1,	False,	False),
						ScriptCard(27,	'Morocco',						ROMANCE,	[SW, BD],		5000,	2000,	3,	1,	False,	True),
						ScriptCard(28,	'The Shop Around the Corner',	ROMANCE,	[S, BD],		6000,	3000,	3,	2,	False,	True),
						ScriptCard(29,	'The Gilded Lily',				ROMANCE,	[S, BD, BD],	4000,	1000,	2,	0,	False,	False),
						ScriptCard(30,	'No Time for Love',				ROMANCE,	[S, BD],		6000,	2000,	3,	1,	False,	True),
						ScriptCard(31,	'The Philadelphia Story',		ROMANCE,	[FH, S, BD],	4000,	2000,	2,	1,	False,	False)])
HORRORDECK	= Deck([	ScriptCard(32,	'Bride of Frankenstein',		HORROR,		[C, SW],		7000,	3000,	3,	2,	False,	True),
						ScriptCard(33,	'Faust',						HORROR,		[DM],		 	5000,	3000,	2,	2,	False,	False),
						ScriptCard(34,	'Freaks',						HORROR,		[DM, C],		5000,	2000,	2,	0,	False,	False),
						ScriptCard(35,	'The Mummy',					HORROR,		[C],			7000,	4000,	3,	2,	False,	False),
						ScriptCard(36,	'The Night of the Hunter',		HORROR,		[DM, S],		5000,	3000,	2,	2,	False,	False),
						ScriptCard(37,	'Dead of Night',				HORROR,		[C],			8000,	4000,	3,	1,	False,	False),
						ScriptCard(38,	'Nosferatu',					HORROR,		[C, FH],		7000,	4000,	3,	1,	False,	False),
						ScriptCard(39,	'The Unknown',					HORROR,		[C, DM],		5000,	3000,	2,	2,	False,	False),
						ScriptCard(40,	'The Hunchback of Notre Dame',	HORROR,		[S, C],			7000,	4000,	3,	2,	False,	True),
						ScriptCard(41,	'The Invisible Man',			HORROR,		[DM, S],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(42,	'The Raven',					HORROR,		[DM, C],		6000,	3000,	3,	2,	False,	False),
						ScriptCard(43,	'Dracula',						HORROR,		[C, FH, SW],	6000,	4000,	4,	2,	True,	False),
						ScriptCard(44,	'Frankenstein',					HORROR,		[C, FH, S],		6000,	3000,	3,	2,	True,	False),
						ScriptCard(45,	'King Kong',					HORROR,		[S, FH],		8000,	4000,	4,	2,	True,	False),
						ScriptCard(46,	'The Invisible Ray',			HORROR,		[FH, DM],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(47,	'The Phantom of the Opera',		HORROR,		[S, DM, FH],	6000,	3000,	3,	2,	False,	True)])
COMEDYDECK	= Deck([	ScriptCard(48,	'The Electric House',		COMEDY,		[S, C],		6000,	3000,	2,	2,	False,	False),
						ScriptCard(49,	'The Music Box',		COMEDY,		[C, C],		5000,	2000,	2,	0,	False,	False),
						ScriptCard(50,	'Sherlock, Jr.',		COMEDY,		[C],		6000,	3000,	3,	2,	False,	False),
						ScriptCard(51,	'Limelight',			COMEDY,		[C, S],		7000,	3000,	4,	2,	False,	True),
						ScriptCard(52,	'Arsenic and Old Lace',		COMEDY,		[C, SW],	6000,	4000,	3,	3,	True,	False),
						ScriptCard(53,	'Modern Times',			COMEDY,		[C, S],		6000,	3000,	3,	2,	False,	True),
						ScriptCard(54,	"Singin' in the Rain",		COMEDY,		[C, BD, S],	8000,	4000,	4,	1,	True,	False),
						ScriptCard(55,	'The General',			COMEDY,		[C, S],		6000,	4000,	3,	3,	False,	False),
						ScriptCard(56,	'The Circus',			COMEDY,		[C, C],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(57,	'The Great Dictator',		COMEDY,		[C, C, S],	6000,	3000,	3,	2,	False,	True),
						ScriptCard(58,	'Mr. Smith Goes to Washington',	COMEDY,		[BD, S],	5000,	2000,	3,	1,	True,	False),
						ScriptCard(59,	'City Lights',			COMEDY,		[C, SW, BD],	6000,	2000,	3,	0,	False,	False),
						ScriptCard(60,	"I'm No Angel",			COMEDY,		[SW, C],	6000,	3000,	3,	2,	False,	False),
						ScriptCard(61,	'Cops',				COMEDY,		[C, S],		7000,	3000,	4,	2,	False,	False),
						ScriptCard(62,	'The Tramp',			COMEDY,		[C],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(63,	'The Playhouse',		COMEDY,		[S, C],		6000,	3000,	2,	2,	False,	False)])
EPICDECK	= Deck([	ScriptCard(64,	'Ben-Hur: A Tale of the Christ',EPIC,	[FH, DM, SW, QL],	8000,	3000,	4,	2,	True,	True),
						ScriptCard(65,	'Cleopatra',			EPIC,	[QL, BD, SW],		7000,	3000,	4,	2,	True,	False),
						ScriptCard(66,	"Hell's Angels",		EPIC,	[FH, SW, BD],		12000,	7000,	4,	3,	True,	False),
						ScriptCard(67,	'David Copperfield',		EPIC,	[BD, SW, S, FH],	7000,	4000,	3,	1,	True,	False),
						ScriptCard(68,	'Paths of Glory',		EPIC,	[BD, DM, FH],		6000,	3000,	3,	2,	True,	False),
						ScriptCard(69,	'The Ten Commandments',		EPIC,	[FH, S, QL, DM],	9000,	5000,	5,	3,	True,	True),
						ScriptCard(70,	'The Wizard of Oz',		EPIC,	[S, C, QL, C],		8000,	4000,	4,	2,	True,	True),
						ScriptCard(71,	'Citizen Kane',			EPIC,	[BD, SW, FH],		7000,	4000,	4,	2,	True,	False),
						ScriptCard(72,	'The King of Kings',		EPIC,	[FH, S, DM],		6000,	3000,	3,	2,	True,	False),
						ScriptCard(73,	'The Great Bank Robbery',	EPIC,	[DM, BD, FH],		5000,	3000,	2,	2,	True,	False),
						ScriptCard(74,	'Birth of a Nation',		EPIC,	[BD, S, DM],		6000,	3000,	3,	2,	True,	False),
						ScriptCard(75,	'The Last Days of Pompei',	EPIC,	[FH, DM, SW, S],	8000,	5000,	3,	3,	True,	False),
						ScriptCard(76,	'The Grapes of Wrath',		EPIC,	[FH, FH, S],		6000,	3000,	3,	2,	True,	True),
						ScriptCard(77,	'The Crusades',			EPIC,	[FH, DM, SW],		7000,	4000,	3,	3,	True,	False),
						ScriptCard(78,	'The African Queen',		EPIC,	[DM, QL, BD],		6000,	3000,	3,	2,	True,	True),
						ScriptCard(79,	'Gone with the Wind',		EPIC,	[BD, QL, SW, FH],	10000,	6000,	5,	3,	True,	True)])
SWORDSDECK	= Deck([	ScriptCard(80,	'Red Dusk',				SWORDS,	[SW, DM],	6000,	3000,	3,	2,	False,	False),
						ScriptCard(81,	'Fighting Caravans',			SWORDS,	[FH],		5000,	2000,	3,	1,	False,	False),
						ScriptCard(82,	'The Four Horsemen of the Apocalypse',	SWORDS,	[FH, DM, S],	6000,	4000,	3,	3,	False,	True),
						ScriptCard(83,	'The Black Pirate',			SWORDS,	[DM, SW, FH],	4000,	2000,	2,	1,	False,	False),
						ScriptCard(84,	'The Sheik',				SWORDS,	[FH, S],	8000,	3000,	4,	2,	True,	False),
						ScriptCard(85,	'The Prince and the Pauper',		SWORDS,	[FH, SW],	5000,	2000,	3,	1,	False,	True),
						ScriptCard(86,	'The Quest of Life',			SWORDS,	[FH, BD],	4000,	1000,	2,	0,	False,	False),
						ScriptCard(87,	'The Adventures of Robin Hood',		SWORDS,	[FH],		7000,	4000,	4,	3,	False,	False),
						ScriptCard(88,	'The Falcon',				SWORDS,	[BD, FH],	6000,	3000,	3,	2,	False,	False),
						ScriptCard(89,	'This Gun for Hire',			SWORDS,	[SW, FH, DM],	6000,	2000,	3,	0,	False,	False),
						ScriptCard(90,	'Jesse James',				SWORDS,	[FH, BD],	6000,	3000,	3,	2,	False,	False),
						ScriptCard(91,	"A Rogue's Romance",			SWORDS,	[FH, SW],	4000,	1000,	2,	0,	False,	False),
						ScriptCard(92,	'The Avenging Sword',			SWORDS,	[FH, SW],	9000,	5000,	4,	3,	False,	False),
						ScriptCard(93,	'The Soldier and the Lady',		SWORDS,	[FH, S],	7000,	4000,	3,	2,	True,	False),
						ScriptCard(94,	'The Count of Monte Cristo',		SWORDS,	[FH, BD, C],	5000,	2000,	3,	1,	False,	True),
						ScriptCard(95,	'Adventures of Don Juan',		SWORDS,	[FH, S, SW],	4000,	2000,	2,	1,	False,	False),
						ScriptCard(96,	'The Thief of Bagdad',			SWORDS,	[FH, C, DM],	5000,	3000,	2,	2,	True,	False)])

CREWDECK	= Deck([	CrewCard(ORDINARYCREW)] * 5 + [CrewCard(GOODCREW)] * 7 + [CrewCard(EXCELLENTCREW)] * 5)
WRITERSDECK	= Deck([	WriterCard(ORDINARYWRITER)] * 10 + [WriterCard(EXCELLENTWRITER)] * 8)
