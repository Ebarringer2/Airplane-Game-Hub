import game.game.tictactoe
import network.server
import interface.ui
import pygame as pg

def click():
    print("Server clicked")

pg.init()
done = False
screen = pg.display.set_mode((480, 500))
clock = pg.time.Clock()
grid = game.game.tictactoe.TicTacToe(
    50,
    50,
    screen,
    "circle",
    400,
    onclick=click
)

server = network.server.TicTacToeServer()
server.start_server()

while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        grid.check_click(event)
        if event.type == pg.QUIT:
            done = True
    server.read_board(grid.grid_drawings)
    grid.draw_grid()
    pg.display.flip()
    clock.tick(60)
server.close_server()
pg.quit()