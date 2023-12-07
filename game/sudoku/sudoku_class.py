import sys
import pygame
from random import randint
from typing import List

class Sudoku:
    def __init__(self):
		# init consts for the obj
        self.x = 0
        self.y = 0
        self.dif = 500 / 9
        self.val = 0
		# init pygame bases
        pygame.font.init()
        self.font1 = pygame.font.SysFont('arial', 18)
        self.screen = pygame.display.set_mode((500, 600))
        # init with empty board
        self.grid = [
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0]
	    ]
    # drawing on the pygame window    
    def draw(self):
        for i in range (9):
            for j in range (9):
                if self.grid[i][j]!= 0:

				    # Fill blue color in already numbered grid
                    pygame.draw.rect(self.screen, (0, 153, 153), (i * self.dif, j * self.dif, self.dif + 1, self.dif + 1))

				    # Fill grid with default numbers specified
                    text1 = self.font1.render(str(self.grid[i][j]), 1, (0, 0, 0))
                    self.screen.blit(text1, (i * self.dif + 15, j * self.dif + 15))
	# Draw lines horizontally and verticallyto form grid		 
        for i in range(10):
            if i % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.dif), (500, i * self.dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.dif, 0), (i * self.dif, 500), thick)	
    # checking validity of a num pos
    def is_valid(self, row, col, num):
        # check if num is already present
        if num in self.grid[row] or num in [self.grid[i][col] for i in range(9)]:
            return False
        # check if num is present in 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True
    # solving algorithm using backtracking
    def solve(self, i, j):
        while self.grid[i][j] != 0:
            if i < 8:
                i += 1
            elif i == 8 and j < 8:
                i = 0
                j += 1
            elif i == 8 and j == 8:
                return True
        pygame.event.pump()
        for it in range(1, 10):
            if self.is_valid(self.grid, i, j, it):
                self.grid[i][j] = it
                global x, y
                x = i
                y = j
                self.screen.fill((255, 255, 255))
                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(20)
                if self.solve(self.grid, i, j) == 1:
                    return True
                else:
                    self.grid[i][j] = 0
                self.screen((255, 255, 255))

                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(50)
        return False
    # method to create the puzle
    def generate_sudoku(self):
        # init with empty 9x9 grid
        board = [[0 for _ in range(9)] for _ in range(9)]
        # fill the grid using the solve method
        for i in range(9):
            for j in range(9):
                self.solve(board, i, j)
        # remove some digits to create the puzzle
        for _ in range(randint(90, 100)):
            row, col = randint(0, 8), randint(0, 8)
            board[row][col] = 0
        return board
    # getting cords for the mouse
    def get_cord(self, pos):
        global x, y
        x = pos[0] // self.dif
        y = pos[1] // self.dif
    # highlight selected cell
    def draw_box(self):
        for i in range(2):
            pygame.draw.line(self.screen, (255, 0, 0), (x * self.dif-3, (y + i)*self.dif), (x * self.dif + self.dif + 3, (y + i)*self.dif), 7)
            pygame.draw.line(self.screen, (255, 0, 0), ( (x + i)* self.dif, y * self.dif ), ((x + i) * self.dif, y * self.dif + self.dif), 7) 
    # fill cell with entered val
    def draw_val(self, val):
        text1 = self.font1.render("wrong", 1, (0, 0, 0))
        self.screen.blit(text1, (x * self.dif + 15, y * self.dif + 15))
