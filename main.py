import pages
from interface.ui import PageGroup
from settings import *
import pygame as pg

pg.init()
done = False
window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

home_page = pages.Home(window)
game_select = pages.GameSelect(window)
pg1 = PageGroup()
pg1.add(home_page, "home")
pg1.add(game_select, "gs")
pg1.select_page("home")

def go_home():
    pg1.select_page("home")

def go_game():
    pg1.select_page("gs")

home_page.button.settings["onclick"] = go_game
game_select.button.settings["onclick"] = go_home

while not done:
    window.fill((255, 255, 255))
    for event in pg.event.get():
        pg1.update_event(event)
        if event.type == pg.QUIT:
            done = True
    pg1.update_auto()
    pg.display.flip()
    clock.tick(60)
pg.quit()