import pygame as pg
import game.utils.output

pg.init()
done = False
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
text = game.utils.output.Text(window=screen, font=pg.font.Font(None, 32))
text.write(50, 50, "This is an example piece of text", "example_text_1")
text.write(50, 80, "This is an example piece of text", "example_text_2")
mode = "stable"
changed = False
while not done:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                mode = "changed"
    if mode == "changed" and not changed:
        text.edit_text("example_text_1", text="This is changed")
        text.remove("example_text_2")
        changed = True
    text.draw()
    pg.draw.line(screen, "red", (60, 80), (130, 100))
    pg.display.flip()
    clock.tick(60)
pg.quit()