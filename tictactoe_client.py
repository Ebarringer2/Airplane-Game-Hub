import game.game.tictactoe
import network.client
import pygame as pg

def click():
    print("Client clicked")

pg.init()
done = False
pg.display.set_caption("Client")
screen = pg.display.set_mode((480, 500))
clock = pg.time.Clock()
grid = game.game.tictactoe.TicTacToe(
    50,
    50,
    screen,
    "cross",
    400,
    onclick=click
)

client = network.client.TicTacToeClient(grid)
key = input("Enter key: ")
client.decode_client_key(key)
client.start_client()

while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        grid.check_click(event)
        if event.type == pg.QUIT:
            done = True
    client.read_board(grid.grid_drawings)
    print(client.board)
    grid.set_board([i for i in client.board.values()])
    grid.draw_grid()
    pg.display.flip()
    clock.tick(60)
client.close_client()
pg.quit()
quit()