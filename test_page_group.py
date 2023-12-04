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
t = game.utils.input.Textbox(50, 80, font=pg.font.Font(None, 32), window=screen,
                    enter_command=enter, filler_text="Enter key")

text = game.utils.output.Text(window=screen, font=pg.font.Font(None, 32))
text.write(50, 50, "Room ID:", "room_id")

t2 = game.utils.input.Textbox(50, 80, font=pg.font.Font(None, 32), window=screen,
                    enter_command=enter, filler_text="Enter pass")

text2 = game.utils.output.Text(window=screen, font=pg.font.Font(None, 32))
text2.write(50, 50, "Password:", "pwd")

page1 = interface.ui.Page()
el_g = [
    (t, t.update_draw, "t_in", "event", [t.update_input]),
    (text, text.draw, "t_out")
]

page2 = interface.ui.Page()
el_g_ = [
    (t2, t2.update_draw, "t_in", "event", [t2.update_input]),
    (text2, text2.draw, "t_out")
]

for _ in el_g:
    page1.add(*_)

for _ in el_g_:
    page2.add(*_)

page_group = interface.ui.PageGroup()
page_group.add(page1, "p1")
page_group.add(page2, "p2")
page_group.select_page("p1")


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