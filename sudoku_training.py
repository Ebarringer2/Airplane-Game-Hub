# file for training the sudoku ml 

# needed imports
from game.sudoku.sudoku_class import Sudoku 
from models.sml import SML 
from models.smlt import SMLT
import pygame as pg

# instantiate the classes
pg.init()
w = pg.display.set_mode((500, 600))
# instantiate the sudoku object with the pygame window
s = Sudoku(window=w)
# instantiate the SML with the unsolved board in the sudoku object
sml = SML(s.unsolved_board)
# instantiate the SMLT with the training data file path and the sml object
smlt = SMLT(data_file='./solutions.txt', sml=sml, window=w)
# start the training loop
smlt.run(epochs=32, g_iterations=100)