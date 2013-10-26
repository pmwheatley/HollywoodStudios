import random
import time
from Constants import *

global genreDie, boxOfficeDie

# Die Class
class Die():
    def __init__(self, sides, values):
        self._sides = sides
        self.values = values
    def roll(self):
        number = random.randint(0, self._sides-1)
        if self.values != []:
            return self.values[number]
        else:
            return number

#random.seed(time.time())
random.seed(GAMESEED)
genreDie = Die(6, GENRES)
boxOfficeDie  = [Die(6, BDICE), Die(6, ADICE)]
