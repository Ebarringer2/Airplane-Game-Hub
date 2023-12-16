# this file uses the dancing links and sudoku solving algorithms to solve the board

# import the needed classes
from game.sudoku.sudoku_class import Sudoku
import game.sudoku.sudoku_class 
import interface.ui
import pygame as pg 
import threading
# instantiate the object 
pg.init()
# create the window 
window = pg.display.set_mode((500, 600)) 
sudoku = game.sudoku.sudoku_class.Sudoku(window) 
# use threading for the run loop
'''def sudoku_solver(sudoku : Sudoku):
    sudoku.solver_run() 
solver_thread = threading.Thread(target=sudoku_solver, args=(sudoku,))
solver_thread.start()'''
# use the dancing links solver specifically 
sudoku.solver_run() 
# instantiate the page 
page = interface.ui.Page()
# 'add something idk'
page.add(sudoku, sudoku.update, "sudoku", "event", [sudoku.handle_input])
# begin the run loop
done = False 
clock = pg.time.Clock()
while not done:
    window.fill((255, 255, 255))
    for event in pg.event.get():
        page.update_event(event) 
        if event.type == pg.QUIT:
            done = True 
    page.update_auto()
    pg.display.flip() 
    clock.tick(60)
pg.quit()