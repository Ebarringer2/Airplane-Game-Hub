import pygame as pg
from typing import Union

class Text:
    def __init__(self, window: pg.display,
                 font: pg.font.Font, color: pg.Color = pg.Color("black")):
        self.window: pg.display = window
        self.font: pg.font.Font = font
        self.color: pg.Color = color
        self.blit_l: dict = {}
    
    def write(self, x: int, y: int, text: str, id: str,
              written_font: Union[pg.font.Font, None] = None,
              written_color: Union[pg.Color, None] = None) -> None:
        """
        Add text to write when draw() is called
        """

        if not written_font:
            written_font: pg.font.Font = self.font
        if not written_color:
            written_color: pg.font.Font = self.color
        if id not in self.blit_l:
            self.blit_l[id] = [written_font, [text, True, written_color], [x, y]]
        else:
            raise KeyError(f"'{id}' already in text dictionary... Pick another key")
    
    def draw(self) -> None:
        """
        Write all text to screen
        """

        for text in self.blit_l.values():
            txt_surface = text[0].render(*text[1])
            self.window.blit(txt_surface, text[2])
        
    def edit_text(self, id: str, x: Union[int, None] = None, y: Union[int, None] = None,
                  text: Union[str, None] = None,
                  written_font: Union[pg.font.Font, None] = None,
                  written_color: Union[pg.Color, None] = None) -> None:
        """
        Edit existing text objects
        """

        if x is None:
            x: int = self.blit_l[id][2][0]
        if y is None:
            y: int = self.blit_l[id][2][1]
        if written_font is None:
            written_font: pg.font.Font = self.blit_l[id][0]
        if written_color is None:
            written_color: pg.Color = self.blit_l[id][1][2]
        if text is None:
            text: str = self.blit_l[id][1][0]
        
        self.blit_l[id] = [written_font, [text, True, written_color], [x, y]]
    
    def remove(self, id: str) -> None:
        """
        Remove text from screen
        """
        try:
            del self.blit_l[id]
        except KeyError:
            print(f"Cannot delete text object with key {id} from screen")
    
    def clear(self) -> None:
        self.blit_l = {}