# example usage of the sudoku solving model 

# import necessary modules
import game.sudoku.sudoku_class
from models.sudoku import SML
import pygame as pg 
# instantiate the objects
pg.init()
window = pg.display.set_mode((500, 600))
sudoku = game.sudoku.sudoku_class.Sudoku(window)
model = SML(sudoku.grid)
# run 
sudoku.generate_sudoku()
sudoku.run()
