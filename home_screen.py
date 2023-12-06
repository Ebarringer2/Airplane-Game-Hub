import interface.ui
import game.utils.input
import game.utils.output
import pygame as pg

WIDTH = 1000
HEIGHT = 800

pg.init()
done = False
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
button = game.utils.input.Button(screen, {
    "paddingx" : 20,
    "paddingy" : 10,
    "x_pos" : WIDTH//2-20,
    "y_pos" : HEIGHT//2-20,
    "timer" : 5,
    "outline" : True,
    "button_color" : pg.color.Color("white"),
    "clicked_color" : pg.color.Color("gray"),
    "text_color" : pg.color.Color("black")
    })


text = game.utils.output.Text(window=screen, font=pg.font.Font(None, 32))
text.write(WIDTH//2, HEIGHT//2-30, "HOME", "room_id")

page_group = interface.ui.Page()
el_g = [
    (button, button.draw, "t_in", "event", [button.check_click]),
    (text, text.draw, "t_out")
]

for _ in el_g:
    page_group.add(*_)

while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        page_group.update_event(event)
        if event.type == pg.QUIT:
            done = True
    page_group.update_auto()
    pg.display.flip()
    clock.tick(60)
pg.quit()