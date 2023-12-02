# import from previous directories
import pygame as pg
from typing import Union
from typing import List

class TicTacToe:
    def __init__(self, pos_x: int, pos_y: int, window: pg.display, type: str,
                 size: int, line_weight: int = 5, color: str = "black",
                 onclick = None, args: tuple = (), spacing: float = 4/5,
                 winning_color: str = "red"):
        self.size: int = size
        self.line_weight: int = line_weight
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.window: pg.display = window
        self.color: str = color
        self.increment: int = self.size // 3
        self.grid_rects: List[pg.Rect] = [
            # Row 1
            pg.Rect(self.pos_x, self.pos_y, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment, self.pos_y, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment*2, self.pos_y, self.increment, self.increment),

            # Row 2
            pg.Rect(self.pos_x, self.pos_y+self.increment, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment, self.pos_y+self.increment, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment*2, self.pos_y+self.increment, self.increment, self.increment),

            # Row 3
            pg.Rect(self.pos_x, self.pos_y+self.increment*2, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment, self.pos_y+self.increment*2, self.increment, self.increment),
            pg.Rect(self.pos_x+self.increment*2, self.pos_y+self.increment*2, self.increment, self.increment),
        ]
        self.grid_drawings: list = [None for box in range(9)]
        self.onclick = onclick
        self.args: tuple = args
        self.spacing: float = spacing
        self.has_won: bool = False
        self.winning_line: Union[tuple, None] = None
        self.winning_color = winning_color
    
    def draw_grid(self) -> None:
        """
        Draw all X's and O's in the grid & draw the grid
        itself to the screen
        """
        # draw gridlines
        for column in range(2):
            pg.draw.line(self.window, self.color, (self.pos_x+(column+1)*self.increment, self.pos_y),
                         (self.pos_x+(column+1)*self.increment, self.pos_y+self.size), self.line_weight)
            
        for row in range(2):
            pg.draw.line(self.window, self.color, (self.pos_x, self.pos_y+(row+1)*self.increment),
                         (self.pos_x+self.size, self.pos_y+(row+1)*self.increment), self.line_weight)
        
        for _type, position in zip(self.grid_drawings, self.grid_rects):
            # draw all X's onto grid
            if _type == "cross":
                pg.draw.line(self.window, self.color, (position.x + (self.increment - self.increment * self.spacing),
                                                       position.y+ (self.increment - self.increment * self.spacing)),
                             (position.x + self.increment * self.spacing, position.y + self.increment * self.spacing),
                             self.line_weight*2)
                pg.draw.line(self.window, self.color, (position.x + (self.increment - self.increment * self.spacing), 
                                                       position.y + self.increment * self.spacing),
                             (position.x + self.increment * self.spacing, position.y + (self.increment - self.increment * self.spacing)),
                             self.line_weight*2)
                
            # draw all O's onto grid
            elif _type == "circle":
                pg.draw.circle(self.window, self.color, (position.x + self.increment//2,
                                                       position.y + self.increment//2),
                               (self.increment * self.spacing)//2, self.line_weight)
        
        if self.winning_line:
            pg.draw.line(*self.winning_line)
                
    def check_click(self, event) -> None:
        """
        Check if any box has been clicked and update positions
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            for box in range(len(self.grid_rects)):
                if self.grid_rects[box].collidepoint(event.pos):
                    if not self.grid_drawings[box]:
                        self.grid_drawings[box] = "cross"

                    if self.onclick:
                        try:
                            self.onclick(*self.args, number=box+1)
                        except TypeError:
                            self.onclick(*self.args)

            winner = self.check_for_winner()

            if winner:
                self.has_won = True
                self.winning_line = (self.window, self.winning_color, winner[1], winner[2], self.line_weight*2)

    def check_for_winner(self) -> Union[str, None]:
        # horizontally check for winner
        for _ in range(3):
            row_start = _*3
            if self.grid_drawings[row_start] and (self.grid_drawings[row_start], self.grid_drawings[row_start+1])\
                == (self.grid_drawings[row_start+1], self.grid_drawings[row_start+2]):
                return self.grid_drawings[row_start], (self.pos_x, self.pos_y+self.increment*_+self.increment//2), (self.pos_x+self.size, self.pos_y+self.increment*_+self.increment//2)

        
        # vertically check for winner
        for _ in range(3):
            start, mid, end = _, _+3, _+6
            if self.grid_drawings[start] and (self.grid_drawings[start], self.grid_drawings[mid])\
                == (self.grid_drawings[mid], self.grid_drawings[end]):
                return self.grid_drawings[start], (self.pos_x+self.increment*_+self.increment//2, self.pos_y), (self.pos_x+self.increment*_+self.increment//2, self.pos_y+self.size)
        
        # diagonally check for winner
        start, mid, end = 0, 4, 8
        if self.grid_drawings[start] and (self.grid_drawings[start], self.grid_drawings[mid])\
                == (self.grid_drawings[mid], self.grid_drawings[end]):
                return self.grid_drawings[start], (self.pos_x, self.pos_y), (self.pos_x+self.size, self.pos_y+self.size)
        start, mid, end = 2, 4, 6
        if self.grid_drawings[start] and (self.grid_drawings[start], self.grid_drawings[mid])\
                == (self.grid_drawings[mid], self.grid_drawings[end]):
                return self.grid_drawings[start], (self.pos_x+self.size, self.pos_y), (self.pos_x, self.pos_y+self.size)
    
    def clear_board(self) -> None:
        self.grid_drawings = [None for box in range(9)]
        self.winning_line = None