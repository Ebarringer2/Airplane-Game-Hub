import pygame as pg

class Textbox:
    def __init__(self, pos_w: int, pos_h: int, font: pg.font.Font,
                 window: pg.display, enter_command, args: tuple=None,
                 size_w: int=140, size_h: int=30, inactive_color: pg.Color=pg.Color('lightskyblue3'),
                 active_color: pg.Color=pg.Color('dodgerblue2'),
                 filler_text: str="", filler_color: pg.Color = pg.Color("gray"),
                 text_color: pg.Color=pg.Color("white"),
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
        if self._enter_command:
            raise
        self._enter_command = command

    def update(self, event) -> None:
        self.check_select(event)
        self.type_text(event)
        self.draw()

    def execute_enter(self) -> None:
        """
        Execute custom command when RETURN key
        is pressed
        """
        if not self.args:
            self._enter_command(text=self._text)
        else:
            self.enter_command(*self.args, text=self._text)

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
                    elif event.key == pg.K_v and event.mod & pg.KMOD_CTRL:
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