import interface.ui
import game.utils.input
import game.utils.output
import game.game.tictactoe
import network.client, network.server
import pygame as pg
from settings import *

# Home
class Home(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window


        self.play = game.utils.input.Button(self.window, {
            "paddingx" : 30,
            "paddingy" : 15,
            "x_pos" : WIDTH//2-73,
            "y_pos" : HEIGHT//2-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Play",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        self.info = game.utils.input.Button(self.window, {
            "paddingx" : 33,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-73,
            "y_pos" : HEIGHT//2+40,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Info",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(250, 110, "Airplane Game Hub", "title")
        
        self.element_group = [
            (self.play, self.play.draw, "play", "event", [self.play.check_click]),
            (self.info, self.info.draw, "info", "event", [self.info.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Info
class Info_Select(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window

        self.tictactoe = game.utils.input.Button(self.window, {
            "paddingx" : 41.5,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-130,
            "y_pos" : HEIGHT//2-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "TicTacToe",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        self.sudoku = game.utils.input.Button(self.window, {
            "paddingx" : 62,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-130,
            "y_pos" : HEIGHT//2+40,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Sudoku",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(250, 110, "Airplane Game Hub", "title")
        
        self.element_group = [
            (self.sudoku, self.sudoku.draw, "sudoku", "event", [self.sudoku.check_click]),
            (self.tictactoe, self.tictactoe.draw, "tictactoe", "event", [self.tictactoe.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Info -> TicTacToe
class Info_TicTacToe(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window
        
        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.body = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 30))
        self.text.write(250, 110, "Airplane Game Hub", "title")
        self.body.write(135, 300, "To play TicTacToe, you can either join a room or start one.", "line1")
        self.body.write(135, 300+TEXT_SPACING, "You can join a room using the unique key that only the host", "line2")
        self.body.write(135, 300+TEXT_SPACING*2, "can access. If someone starts a room, they always will start", "line3")
        self.body.write(135, 300+TEXT_SPACING*3, "first and get to place their \"piece\" on the board first.", "line4")
        self.body.write(135, 300+TEXT_SPACING*4, "The person who starts the room will place circles, while the", "line5")
        self.body.write(135, 300+TEXT_SPACING*5, "one who starts the room will place crosses.", "line6")           
        
        self.element_group = [
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out"),
            (self.body, self.body.draw, "body_text")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Info -> Sudoku
class Info_Sudoku(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window
        
        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.body = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 30))
        self.text.write(250, 110, "Airplane Game Hub", "title")
        
        self.body.write(135, 300, "Complete a 9x9 grid by placing numbers 1-9 in each row,", "line1")
        self.body.write(135, 300+TEXT_SPACING, "column, and 3x3 subgrid. Begin with provided clues, avoiding", "line2")
        self.body.write(135, 300+TEXT_SPACING*2, "duplicates in rows, columns, or subgrids. Use logic to deduce", "line3")
        self.body.write(135, 300+TEXT_SPACING*3, "missing numbers and steadily fill the entire grid.", "line4")
        
        self.element_group = [
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out"),
            (self.body, self.body.draw, "body_text")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Play
class GameSelect(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window


        self.tictactoe = game.utils.input.Button(self.window, {
            "paddingx" : 41.5,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-130,
            "y_pos" : HEIGHT//2-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "TicTacToe",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        self.sudoku = game.utils.input.Button(self.window, {
            "paddingx" : 62,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-130,
            "y_pos" : HEIGHT//2+40,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Sudoku",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })

        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(420, 110, "Games", "title")
        
        self.element_group = [
            (self.sudoku, self.sudoku.draw, "sudoku", "event", [self.sudoku.check_click]),
            (self.tictactoe, self.tictactoe.draw, "tictactoe", "event", [self.tictactoe.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Play -> TicTacToe
class TicTacToeRoomOptions(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window

        self.host_room = game.utils.input.Button(self.window, {
            "paddingx" : 41.5,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-140,
            "y_pos" : HEIGHT//2-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Host Room",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })
        
        self.find_room = game.utils.input.Button(self.window, {
            "paddingx" : 44.5,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-140,
            "y_pos" : HEIGHT//2+40,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Find Room",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 46)
            })

        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(382, 110, "TicTacToe", "title")
        
        self.element_group = [
            (self.host_room, self.host_room.draw, "host_room", "event", [self.host_room.check_click]),
            (self.find_room, self.find_room.draw, "find_room", "event", [self.find_room.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

# Home -> Play -> TicTacToe -> Host Room
class TicTacToeServerPage(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window

        self.grid = game.game.tictactoe.TicTacToe(
            WIDTH//2-200,
            HEIGHT//2-200,
            self.window,
            "cross",
            400
        )

        self.client = network.client.TicTacToeClient(self.grid)

        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(382, 110, "TicTacToe", "title")
        
        self.element_group = [
            (self.client, self.update_client_board, "client", "event", [self.grid.check_click]),
            (self.grid, self.update_ttt_board, "grid", "event", [self.grid.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out"),
        ]

        for element in self.element_group:
            self.add(*element)
    
    def update_ttt_board(self):
        self.grid.set_board([i for i in self.client.board.values()])
        self.grid.draw_grid()
    
    def update_client_board(self):
        self.client.read_board(self.grid.grid_drawings)
    
    def initialize_client(self, key):
        try:
            self.client.decode_client_key(key)
        except:
            raise AttributeError
        self.client.start_client()
    
    def clean_up(self):
        self.client.close_client()

# Home -> Play -> TicTacToe -> Find Room
class TicTacToeRoomFinder(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window

        self.enter_key = game.utils.input.Textbox(
            302, HEIGHT//2-70, pg.font.SysFont("calibri", 30, bold=True),
            self.window, self.filler_func, filler_text="Room Key",
            size_h=40, size_w=400)
        
        self.connect_button = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : WIDTH//2-89,
            "y_pos" : HEIGHT//2,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Connect",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("calibri", 40)
            })

        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        self.wrong_key = False

        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.label = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 50))
        self.error = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 50), color=pg.color.Color((208,4,4)))
        self.text.write(382, 110, "TicTacToe", "title")
        self.label.write(342, HEIGHT//2-120, "Enter Room Key:", "enter_key")
        
        self.element_group = [
            (self.error, self.error.draw, "error"),
            (self.enter_key, self.enter_key.update_draw, "find_room", "event", [self.enter_key.update_input]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.connect_button, self.connect_button.draw, "connect_button", "event", [self.connect_button.check_click]),
            (self.text, self.text.draw, "text_out"),
            (self.label, self.label.draw, "label")
        ]

        for element in self.element_group:
            self.add(*element)
    
    def filler_func(self, text: str):
        pass

    def get_key(self):
        return self.enter_key.text

    def update_error_msg(self):
        if self.wrong_key:
            self.error.write(WIDTH//2-110, HEIGHT//2-180, "Invalid Key", "error_msg")
        else:
            self.error.clear()

# Home -> Play -> TicTacToe -> Find Room -> Connect
class TicTacToeClientPage(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window

        self.grid = game.game.tictactoe.TicTacToe(
            WIDTH//2-200,
            HEIGHT//2-200,
            self.window,
            "cross",
            400
        )

        self.client = network.client.TicTacToeClient(self.grid)

        self.back = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 12,
            "x_pos" : 20,
            "y_pos" : HEIGHT-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((232,100,100)),
            "clicked_color" : pg.color.Color((208,4,4)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            "outline_color" : pg.color.Color((208,4,4)),
            "font" : pg.font.SysFont("calibri", 30, bold=True)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("calibri", 64))
        self.text.write(382, 110, "TicTacToe", "title")
        
        self.element_group = [
            (self.client, self.update_client_board, "client", "event", [self.grid.check_click]),
            (self.grid, self.update_ttt_board, "grid", "event", [self.grid.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out"),
        ]

        for element in self.element_group:
            self.add(*element)
    
    def update_ttt_board(self):
        self.grid.set_board([i for i in self.client.board.values()])
        self.grid.draw_grid()
    
    def update_client_board(self):
        self.client.read_board(self.grid.grid_drawings)
    
    def initialize_client(self, key):
        try:
            self.client.decode_client_key(key)
        except:
            raise AttributeError
        self.client.start_client()
    
    def clean_up(self):
        self.client.close_client()
        self.grid.reset()