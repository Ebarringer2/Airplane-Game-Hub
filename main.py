import pages
from interface.ui import PageGroup
from settings import *
import pygame as pg

# initialize game
pg.init()
done = False
clock = pg.time.Clock()

# initialize window
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Airplane Game Hub")

# easter egg :)
print("🦖")

# initialize all screens to be displayed
home_page = pages.Home(window)

info_select = pages.Info_Select(window)
info_tic_tac_toe = pages.Info_TicTacToe(window)
info_sudoku = pages.Info_Sudoku(window)

game_select = pages.GameSelect(window)

tic_tac_toe_room_options = pages.TicTacToeRoomOptions(window)
tic_tac_toe_room_finder = pages.TicTacToeRoomFinder(window)
tic_tac_toe_client_screen = pages.TicTacToeClientPage(window)

# add all pages to page manager
page_list = [
    (home_page, "home"),
    (info_select, "info_select"),
    (info_tic_tac_toe, "info_tic_tac_toe"),
    (info_sudoku, "info_sudoku"),
    (game_select, "game_select"),
    (tic_tac_toe_room_options, "tic_tac_toe_room_options"),
    (tic_tac_toe_room_finder, "tic_tac_toe_room_finder"),
    (tic_tac_toe_client_screen, "tic_tac_toe_client_screen")
]

all_pages = PageGroup()
for page in page_list:
    all_pages.add(page[0], page[1])

# select page to be shown on start screen
all_pages.select_page("home")

# define all button functions
def select_game_select_screen(): all_pages.select_page("game_select")
def select_home_screen(): all_pages.select_page("home")
def select_info_select_screen(): all_pages.select_page("info_select")
def select_info_tic_tac_toe_screen(): all_pages.select_page("info_tic_tac_toe")
def select_info_sudoku_screen(): all_pages.select_page("info_sudoku")
def select_tic_tac_toe_room_options_screen(): all_pages.select_page("tic_tac_toe_room_options")

def select_tic_tac_toe_room_finder_screen():
    tic_tac_toe_room_finder.wrong_key = False
    tic_tac_toe_room_finder.update_error_msg()
    all_pages.select_page("tic_tac_toe_room_finder")

def select_tic_tac_toe_client_screen():
    try:
        tic_tac_toe_client_screen.initialize_client(tic_tac_toe_room_finder.get_key())
        all_pages.select_page("tic_tac_toe_client_screen")
    except:
        tic_tac_toe_room_finder.wrong_key = True
        tic_tac_toe_room_finder.update_error_msg()

def exit_tic_tac_toe_client():
    tic_tac_toe_client_screen.clean_up()
    all_pages.select_page("tic_tac_toe_room_finder")


# bind all home button functions
home_page.play.settings["onclick"] = select_game_select_screen
home_page.info.settings["onclick"] = select_info_select_screen

# bind all info select button functions
info_select.back.settings["onclick"] = select_home_screen
info_select.tictactoe.settings["onclick"] = select_info_tic_tac_toe_screen
info_select.sudoku.settings["onclick"] = select_info_sudoku_screen

# bind all info for tictactoe button functions
info_tic_tac_toe.back.settings["onclick"] = select_info_select_screen

# bind all info for sudoku button functions
info_sudoku.back.settings["onclick"] = select_info_select_screen

# bind all game select button functions
game_select.back.settings["onclick"] = select_home_screen
game_select.tictactoe.settings["onclick"] = select_tic_tac_toe_room_options_screen

# bind all tictactoe game options button functions
tic_tac_toe_room_options.back.settings["onclick"] = select_game_select_screen
tic_tac_toe_room_options.find_room.settings["onclick"] = select_tic_tac_toe_room_finder_screen

tic_tac_toe_room_finder.back.settings["onclick"] = select_tic_tac_toe_room_options_screen
tic_tac_toe_room_finder.connect_button.settings["onclick"] = select_tic_tac_toe_client_screen

tic_tac_toe_client_screen.back.settings["onclick"] = exit_tic_tac_toe_client

# main loop
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