import pages
from interface.ui import PageGroup
from settings import *
import pygame as pg
from emoji import emojize

# initialize game
pg.init()
done = False
clock = pg.time.Clock()

# initialize window
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Airplane Game Hub")

# easter egg :)
print(emojize(":T-Rex:"))
# print(pg.font.get_fonts())

# initialize all screens to be displayed
home_page = pages.Home(window)
info_select = pages.Info_Select(window)
game_select = pages.GameSelect(window)

# add all pages to page manager
all_pages = PageGroup()
all_pages.add(home_page, "home")
all_pages.add(info_select, "info_select")
all_pages.add(game_select, "game_select")

# select page to be shown on start screen
all_pages.select_page("info_select")

# define all button functions
def select_game_select_screen(): all_pages.select_page("game_select")
def select_home_screen(): all_pages.select_page("home")
def select_info_select_screen(): all_pages.select_page("info_select")

# bind all home button functions
home_page.play.settings["onclick"] = select_game_select_screen
home_page.info.settings["onclick"] = select_info_select_screen

# bind all info select button functions
info_select.back.settings["onclick"] = select_home_screen

# bind all game select button functions
game_select.button.settings["onclick"] = select_home_screen

while not done:
    window.fill((255, 255, 255))
    for event in pg.event.get():
        all_pages.update_event(event)
        if event.type == pg.QUIT:
            done = True
    all_pages.update_auto()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()