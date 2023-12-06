import interface.ui
import game.utils.input
import game.utils.output
import pygame as pg

def enter(text):
    print(text)

pg.init()
done = False
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
button = game.utils.input.Button(screen, {"paddingx" : 20, "paddingy" : 10, "timer" : 5, "outline" : True, "button_color" : pg.color.Color("white"), "clicked_color" : pg.color.Color("gray"), "outline_color" : pg.color.Color("white"), "text_color" : pg.color.Color("black")})

page_group = interface.ui.Page()
el_g = [
    (button, button.draw, "t_in", "event", [button.check_click])
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