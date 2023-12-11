# import Sudoku object and UI system
import game.sudoku.sudoku_class
import interface.ui
import pygame as pg
# instantiate the object
pg.init()
window = pg.display.set_mode((500, 600))
sudoku = game.sudoku.sudoku_class.Sudoku(window)
sudoku.generate_sudoku()
sudoku.running = True
# instantiate the page
page = interface.ui.Page()
# add something idk
page.add(sudoku, sudoku.update, "sudoku", "event", [sudoku.handle_input])
# create the puzzle
#sudoku.generate_sudoku()
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