import interface.ui
import game.utils.input
import game.utils.output
import pygame as pg
from settings import *

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
            "font" : pg.font.SysFont("hiraginosansgb", 46)
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
            "font" : pg.font.SysFont("hiraginosansgb", 46)
            })
        
        # create text object for this screen
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("ヒラキノ角コシックw8", 64))
        self.text.write(130, 110, "Airplane Game Hub", "title")
        
        self.element_group = [
            (self.play, self.play.draw, "play", "event", [self.play.check_click]),
            (self.info, self.info.draw, "info", "event", [self.info.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

class Info_Select(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window


        self.tictactoe = game.utils.input.Button(self.window, {
            "paddingx" : 30,
            "paddingy" : 15,
            "x_pos" : WIDTH//2-137,
            "y_pos" : HEIGHT//2-75,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "TicTacToe",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("hiraginosansgb", 46)
            })
        
        self.sudoku = game.utils.input.Button(self.window, {
            "paddingx" : 62,
            "paddingy" : 17.5,
            "x_pos" : WIDTH//2-137,
            "y_pos" : HEIGHT//2+40,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color((204,204,204)),
            "clicked_color" : pg.color.Color((160,156,156)),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Sudoku",
            "outline_color" : pg.color.Color((160,156,156)),
            "font" : pg.font.SysFont("hiraginosansgb", 46)
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
        self.text = game.utils.output.Text(window=self.window, font=pg.font.SysFont("ヒラキノ角コシックw8", 64))
        self.text.write(130, 110, "Airplane Game Hub", "title")
        
        self.element_group = [
            (self.tictactoe, self.tictactoe.draw, "tictactoe", "event", [self.tictactoe.check_click]),
            (self.sudoku, self.sudoku.draw, "sudoku", "event", [self.sudoku.check_click]),
            (self.back, self.back.draw, "back", "event", [self.back.check_click]),
            (self.text, self.text.draw, "text_out")
        ]

        for element in self.element_group:
            self.add(*element)

class GameSelect(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window


        self.button = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 10,
            "x_pos" : WIDTH//2-20,
            "y_pos" : HEIGHT//2-20,
            "timer" : BUTTON_TIMER,
            "outline" : True,
            "button_color" : pg.color.Color("white"),
            "clicked_color" : pg.color.Color("gray"),
            "text_color" : pg.color.Color("black"),
            "display_text" : "Back",
            })
        
        
        self.text = game.utils.output.Text(window=self.window, font=pg.font.Font(None, 32))
        self.text.write(WIDTH//2-10, 10, "GAME SELECT", "room_id")
        
        self.element_group = [
            (self.button, self.button.draw, "t_in", "event", [self.button.check_click]),
            (self.text, self.text.draw, "t_out")
        ]

        for element in self.element_group:
            self.add(*element)