import pygame as pg
from random import randint
from typing import Tuple

class Textbox:
    def __init__(self, pos_w: int, pos_h: int, font: pg.font.Font,
                 window: pg.display, enter_command, args: tuple=None,
                 size_w: int=140, size_h: int=30, inactive_color: pg.Color=pg.Color('lightskyblue3'),
                 active_color: pg.Color=pg.Color('dodgerblue2'),
                 filler_text: str="", filler_color: pg.Color = pg.Color("gray"),
                 text_color: pg.Color=pg.Color("black"),
                 max_char: int=999):
        self.font = font
        self.size_w = size_w
        self.input_box = pg.Rect(pos_w, pos_h, self.size_w, size_h)
        self.text = ""
        self.active = False
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.max_char= max_char
        self.filler_text = filler_text
        self.color = self.inactive_color
        self.window = window
        self._enter_command = enter_command
        self.args = args
        self.filler_color = filler_color
        self.text_color = text_color
        self.display_text = self.text
        pg.scrap.init()
        pg.scrap.set_mode(pg.SCRAP_CLIPBOARD)
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not isinstance(text, str):
            raise ValueError(f"Attempted to assign {type(text)} to {type(str)}")
        self._text = text

    @property
    def enter_command(self):
        return self._enter_command

    @enter_command.setter
    def enter_command(self, command):
        self._enter_command = command

    def update_input(self, event) -> None:
        self.check_select(event)
        self.type_text(event)
    
    def update_draw(self) -> None:
        self.draw()

    def execute_enter(self) -> None:
        """
        Execute custom command when RETURN key
        is pressed
        """
        if not self.args:
            self._enter_command(text=self._text)
        else:
            self._enter_command(*self.args, text=self._text)

    def check_select(self, event) -> None:
        """
        Change input box color if user has clicked box
        """
        if event.type == pg.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
                if self.active:
                    self.color = self.active_color
                else:
                    self.color = self.inactive_color
    
    def type_text(self, event) -> None:
        """
        Allow user to type if box has been selected
        """
        if event.type == pg.KEYDOWN:
                if self.active:
                    if event.key == pg.K_RETURN:
                        self.execute_enter()
                        self.text = ''
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pg.K_v and (event.mod & pg.KMOD_CTRL or event.mod & pg.KMOD_META):
                        paste = pg.scrap.get("text/plain;charset=utf-8").decode().replace("\x00", "")
                        if not len(self.text) + len(paste) > self.max_char:
                            self.text += paste
                    else:
                        if not len(self.text) >= self.max_char:
                            self.text += event.unicode
                    self.display_text = self.text
                    self.update_display_text(self.display_text)
    
    def draw(self) -> None:
        """
        Draw to screen
        """
        if self.text.encode() == b"" and not self.active:
            txt_surface = self.font.render(self.filler_text, True, self.filler_color)
        else:
            txt_surface = self.font.render(self.display_text, True, self.text_color)
        self.window.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        pg.draw.rect(self.window, self.color, self.input_box, 2)
    
    def remaining_text_wrap(self, text) -> int:
        """
        Used for wrapping text. Check how much
        remaining space there is for text
        in the input box.
        """
        return self.size_w-self.font.size(text)[0]
    
    def update_display_text(self, text: str) -> None:
        """
        
        """
        if self.remaining_text_wrap(text) <= 5:
            if self.remaining_text_wrap(text[1:]) <= 5:
                self.update_display_text(text[2:])
            else:
                self.display_text = text[1:]
        else:
            self.display_text = text
    
    def set_enter_command(self, command) -> None:
        """
        Change what happens when return key is clicked
        """
        self._enter_command = command

class Button:
    def __init__(self, window: pg.display, settings: dict = {}):
        """
        Create a button
        """
        self.settings = {
            "onclick" : self.out,
            "id" : randint(1, 100),
            "button_color" : pg.Color("gray"),
            "text_color" : pg.Color("white"),
            "clicked_color" : pg.Color("black"),
            "click_shadow" : True,
            "paddingx" : 5,
            "paddingy" : 5,
            "x_pos" : 100,
            "y_pos" : 100,
            "timer" : 20,
            "counter" : 0,
            "display_text" : "Button",
            "font" : pg.font.Font(None, 32),
            "outline" : False,
            "outline_width" : 3,
            "outline_color" : pg.Color("gray")
        }

        for key, value in  settings.items():
            self.settings[key] = value
        
        if not self.settings["click_shadow"]:
            self.settings["clicked_color"] = self.settings["button_color"]
        
        x_size, y_size = self.text_size()
        self.window = window
        self.start_drop = False
        self.button_rect = pg.Rect(self.settings["x_pos"], self.settings["y_pos"], x_size+2*self.settings["paddingx"], y_size+2*self.settings["paddingy"])
    
    def onclick(self):
        self.settings["onclick"]()
    
    def out(self):
        print(f"{self} was clicked")
    
    def __str__(self):
        return f"<Button Obj {self.settings["id"]}>"

    def draw(self):
        if self.settings["counter"] >= 1 and self.start_drop:
            self.settings["counter"] = 0
            self.start_drop = False
        elif self.settings["counter"] != 1 and self.start_drop:
            self.settings["counter"] += 1/self.settings["timer"]
        
        if self.start_drop:
            color = self.settings["clicked_color"]
        else:
            color = self.settings["button_color"]

        pg.draw.rect(self.window, color, self.button_rect)
        if self.settings["outline"]:
            pg.draw.rect(self.window, self.settings["outline_color"], self.button_rect, self.settings["outline_width"])
        txt_surface = self.settings["font"].render(self.settings["display_text"], True, self.settings["text_color"])
        self.window.blit(txt_surface, (self.settings["x_pos"]+self.settings["paddingx"], self.settings["y_pos"]+self.settings["paddingy"]))
    
    def check_click(self, event) -> None:
        """
        Change button color if clicked
        """
        if event.type == pg.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.start_drop = True
                    self.settings["counter"]
                    self.onclick()
    
    def text_size(self) -> Tuple[int, int]:
        """
        Return size of text in button
        """
        return self.settings["font"].size(self.settings["display_text"])[0], self.settings["font"].size(self.settings["display_text"])[1]