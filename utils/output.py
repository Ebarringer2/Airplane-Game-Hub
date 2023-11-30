import pygame as pg
from typing import Union

class Text:
    def __init__(self, window: pg.display,
                 font: pg.font.Font, color: pg.Color = pg.Color("white")):
        self.window: pg.display = window
        self.font: pg.font.Font = font
        self.color: pg.Color = color
        self.blit_l: list = []
    
    def write(self, text: str,
              written_font: Union[pg.font.Font, None] = None,
              written_color: Union[pg.Color, None] = None):
        if not written_font:
            written_font: pg.font.Font = self.font
        if not written_color:
            written_color: pg.font.Font = self.color
        
        self.blit_l.append((written_font, (text, True, written_color)))
    
    def draw(self, x: int, y: int):
        for text in self.blit_l:
            txt_surface = text[0].render(*text[1])
            self.window.blit(txt_surface, (x, y))