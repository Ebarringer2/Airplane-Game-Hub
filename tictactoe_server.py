import game.game.tictactoe
import network.server
import pygame as pg

def click():
    print("Server clicked")

pg.init()
done = False
pg.display.set_caption("Server")
screen = pg.display.set_mode((480, 500))
pg.scrap.init()
pg.scrap.set_mode(pg.SCRAP_CLIPBOARD)

clock = pg.time.Clock()
grid = game.game.tictactoe.TicTacToe(
    50,
    50,
    screen,
    "circle",
    400,
    onclick=click
)

server = network.server.TicTacToeServer(grid)
server.start_server()
pg.scrap.put(pg.SCRAP_TEXT, server.KEY.encode("utf-8"))
while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        grid.check_click(event)
        if event.type == pg.QUIT:
            done = True
    server.read_board(grid.grid_drawings)
    grid.set_board([i for i in server.board.values()]) 
    grid.draw_grid()
    pg.display.flip()
    clock.tick(60)
server.close_server()
pg.quit()
quit()