import interface.ui
import game.utils.input
import game.utils.output
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

# displays info
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

# displays tictactoe page info
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

# displays tictactoe page info
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
        self.text.write(250, 110, "Airplane Game Hub", "title")
        
        self.element_group = [
            (self.sudoku, self.sudoku.draw, "sudoku", "event", [self.sudoku.check_click]),
            (self.tictactoe, self.tictactoe.draw, "tictactoe", "event", [self.tictactoe.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)