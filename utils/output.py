import pygame as pg
from typing import Union

class Text:
    def __init__(self, window: pg.display,
                 font: pg.font.Font, color: pg.Color = pg.Color("white")):
        self.window: pg.display = window
        self.font: pg.font.Font = font
        self.color: pg.Color = color
        self.blit_l: dict = {}
    
    def write(self, x: int, y: int, text: str, id: str,
              written_font: Union[pg.font.Font, None] = None,
              written_color: Union[pg.Color, None] = None):
        if not written_font:
            written_font: pg.font.Font = self.font
        if not written_color:
            written_color: pg.font.Font = self.color
        if id not in self.blit_l:
            self.blit_l[id] = [written_font, [text, True, written_color], [x, y]]
        else:
            raise KeyError(f"'{id}' already in text dictionary... Pick another key")
    
    def draw(self):
        for text in self.blit_l.values():
            txt_surface = text[0].render(*text[1])
            self.window.blit(txt_surface, text[2])