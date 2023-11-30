# script to initialize the sudoko board with a random setup
from random import randint as r
####### BACKGROUND #######
# the board is a 9x9 grid made up of 9 3x3 smaller square grids
class Board:
    def __init__(self):
        self.sGrid1 = [0, 0, 0]
        self.sGrid2 = [0, 0, 0]
        self.sGrid3 = [0, 0, 0]
        self.sGrid4 = [0, 0, 0]
        self.sGrid5 = [0, 0, 0]
        self.sGrid