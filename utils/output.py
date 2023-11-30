import pygame as pg
from typing import Union

class Text:
    def __init__(self, window: pg.display,
                 font: pg.font.Font, color: pg.Color = pg.Color("white")):
        self.window = window
        self.font = font
        self.color = color
    
    def write(self, x: int, y: int, text: str,
              written_font: Union[pg.font.Font, None] = None,
              written_color: Union[pg.Color, None] = None):
        if not written_font:
            written_font = self.font
        if not written_color:
            written_color = self.color
        
        txt_surface = written_font.render(text, True, written_color)
        self.window.blit(txt_surface, (x, y))