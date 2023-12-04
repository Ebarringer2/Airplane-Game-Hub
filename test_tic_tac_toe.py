import pygame as pg
import game.tictactoe
from game.settings import *

def click(number: int):
    print(f"Board clicked!   |   Box #{number} clicked")

pg.init()
done = False
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
grid = game.tictactoe.TicTacToe(WIDTH//2-200, HEIGHT//2-200, screen, "circle", 400, onclick=click)
while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        grid.check_click(event)
        if event.type == pg.QUIT:
            done = True
    grid.draw_grid()
    pg.display.flip()
    clock.tick(60)
pg.quit()