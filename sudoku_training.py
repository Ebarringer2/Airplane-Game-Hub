# file for training the sudoku ml 

# needed imports
from game.sudoku.sudoku_class import Sudoku 
from models.sml import SML 
from models.smlt import SMLT
import pygame as pg
import interface.ui 

# instantiate the classes
pg.init()
window = pg.display.set_mode((500, 600))
sudoku = Sudoku(window=window)
sml = SML(sudoku=sudoku)
smlt = SMLT(data_file='./solutions.txt', sml=sml)
smlt.run()