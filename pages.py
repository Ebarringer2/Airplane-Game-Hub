import interface.ui
import game.utils.input
import game.utils.output
import pygame as pg
from settings import *

class Home(interface.ui.Page):
    def __init__(self, window: pg.display):
        super().__init__()
        self.window: pg.display = window


        self.button = game.utils.input.Button(self.window, {
            "paddingx" : 20,
            "paddingy" : 10,
            "x_pos" : WIDTH//2-20,
            "y_pos" : HEIGHT//2-20,
            "timer" : 5,
            "outline" : True,
            "button_color" : pg.color.Color("white"),
            "clicked_color" : pg.color.Color("gray"),
            "text_color" : pg.color.Color("black"),
            "display_text" : "PLAY",
            })
        

        self.text = game.utils.output.Text(window=self.window, font=pg.font.Font(None, 32))
        self.text.write(WIDTH//2, HEIGHT//2-30, "HOME", "room_id")
        
        self.element_group = [
            (self.button, self.button.draw, "t_in", "event", [self.button.check_click]),
            (self.text, self.text.draw, "t_out")
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
            "timer" : 5,
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