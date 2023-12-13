import sys
import pygame
from random import randint
from typing import List

class Sudoku:
    def __init__(self, window):
        self.screen = window
		# init consts for the obj
        self.x = 0
        self.y = 0
        self.dif = 500 / 9
        self.val = 0
        # init mutables for the obj
        #self.running = False
        self.flag1 = 0
        self.flag2 = 0
        self.rs = 0
        self.error = 0
        # for updating the solutions
        self.solved = False
        self.generated = False
		# init pygame bases
        pygame.font.init()
        self.font1 = pygame.font.SysFont('arial', 18)
        self.window = window
        # init with empty board
        self.grid = [
		    [7, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 8, 0, 0, 1, 0, 0],
		    [0, 2, 0, 0, 0, 0, 0, 0, 9],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 6, 0, 0, 0],
		    [0, 3, 0, 0, 8, 0, 0, 6, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 4, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 5, 0]
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
	# Draw lines horizontally and vertically to form grid		 
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
            if self.is_valid(i, j, it):
                self.grid[i][j] = it
                global x, y
                x = i
                y = j
                self.screen.fill((255, 255, 255))
                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(20)
                if self.solve(i, j) == 1:
                    return True
                else:
                    self.grid[i][j] = 0
                self.screen.fill((255, 255, 255))

                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(50)
        # update for method
        #self.save_solution()
        self.solved = False
        return False
    # method to check if the grid is solved
    def check_solved(self):
        self.solved = True ## assume grid is solved at first
        if self.generated:  # check if board has been generated to avoid infinite loop
            for i in range(9):
                for j in range(9):
                    if self.grid[i][j] == 0:
                        self.solved = False
        return self.solved
    # method to create the puzle
    def generate_sudoku(self):
        print("Generating Sudoku")
        # init with empty 9x9 grid
        board = [[0 for _ in range(9)] for _ in range(9)]
        # copy the initial state of the grid
        for i in range(9):
            for j in range(9):
                board[i][j] = self.grid[i][j]
        # fill the grid using the solve method
        for i in range(9):
            for j in range(9):
                self.solve(i, j)
        # remove some digits to create the puzzle
        for _ in range(randint(10, 20)):
            print("Removing digits, adding zeroes")
            row, col = randint(0, 8), randint(0, 8)
            board[row][col] = 0
        # update for method
        self.grid = board
        print(self.grid)
        self.generated = True
    # getting cords for the mouse
    def get_cord(self, pos):
        #global x, y
        x = pos[0] // self.dif
        y = pos[1] // self.dif
        # set grid cords to pos of mouse
        self.x = x 
        self.y = y
    # highlight selected cell
    def draw_box(self):
        for i in range(2):
            pygame.draw.line(self.screen, (255, 0, 0), (self.x * self.dif-3, (self.y + i)*self.dif), (self.x * self.dif + self.dif + 3, (self.y + i)*self.dif), 7)
            pygame.draw.line(self.screen, (255, 0, 0), ( (self.x + i)* self.dif, self.y * self.dif ), ((self.x + i) * self.dif, self.y * self.dif + self.dif), 7) 
    # fill cell with entered val
    def draw_val(self, val):
        text1 = self.font1.render("wrong", 1, (0, 0, 0))
        self.screen.blit(text1, (x * self.dif + 15, y * self.dif + 15))
    # raise error for wrong value
    def raise_error1(self):
        text1 = self.font1.render("wrong", 1, (0, 0, 0))
        self.screen.blit(text1, (20, 570))
    def raise_error2(self):
        text1 = self.font1.render("not a valid key", 1, (0, 0, 0))
        self.screen.blit(text1, (20, 570))
    # check if a val entered is valid
    def valid(self, i, j, val):
        for it in range(9):
            if self.grid[i][it] == val:
                return False
            if self.grid[it][j] == val:
                return False
        it = i // 3
        jt = j // 3
        for i in range(it * 3, it * 3 + 3):
            for j in range(jt * 3, jt * 3 + 3):
                if self.grid[i][j] == val:
                    return False
        return True
    # method for displaying instructions
    def instruction(self):
        text1 = self.font1.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
        text2 = self.font1.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
        self.screen.blit(text1, (20, 520))	
    # method for telling the user their position on the screen
    def display_pos(self):
        text1 = self.font1.render("Position: " + " x: " + str(self.x) + " y: " + str(self.y), 1, (0, 0, 0))
        self.screen.blit(text1, (20, 540))
    # method for handling user input
    def handle_input(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.flag1 = 1
            pos = pygame.mouse.get_pos()
            self.get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= 1
                self.flag1 = 1
            if event.key == pygame.K_RIGHT:
                self.x += 1
                self.flag1 = 1
            if event.key == pygame.K_UP:
                self.y -= 1
                self.flag1 = 1
            if event.key == pygame.K_DOWN:
                self.y += 1
                self.flag1 = 1
            # value input handling
            if event.key == pygame.K_1:
                self.val = 1
            if event.key == pygame.K_2:
                self.val = 2
            if event.key == pygame.K_3:
                self.val = 3
            if event.key == pygame.K_4:
                self.val = 4
            if event.key == pygame.K_5:
                self.val = 5
            if event.key == pygame.K_6:
                self.val = 6
            if event.key == pygame.K_7:
                self.val = 7
            if event.key == pygame.K_8:
                self.val = 8
            if event.key == pygame.K_9:
                self.val = 9
            # delete val on backspace
            if event.key == pygame.K_BACKSPACE:
                self.val = 0
            if event.key == pygame.K_RETURN:
                print('solving puzzle')
                self.flag2 = 1
    # run method
    def update(self):
        #self.handle_input() ==> this is done in the UI system
        # process user input
        if self.generated:
            self.check_solved() # check whether or not the board is solved
        if self.solved:
            self.save_solution()
        self.display_pos() # display the user's current pos
        self.draw_box() # updates the position box for the UI
        if self.flag2 == 1:
            if self.solve(0, 0) == False:
                self.error = 1
            else:
                self.rs = 1
        if self.val != 0:
            self.draw_val(self.val)
            if self.valid(int(self.x), int(self.y), self.val):
                self.grid[int(self.x)][int(self.y)] = self.val
                self.flag1 = 0
            else:
                self.grid[int(self.x)][int(self.y)] = 0
                self.raise_error2()
            self.val = 0
        # handle errors
        if self.error == 1:
            self.raise_error1()
        self.draw()
        if self.flag1 == 1:
            self.draw_box()
        self.instruction()
        # update window
        pygame.display.update()
    # run loop
    def run(self):
        self.running = True
        print(self.running)
        self.generate_sudoku()
        while self.running:
            # white background
            self.screen.fill((255, 255, 255))
            # update in run loop
            self.update()
    # save past solutions so that we can save time solving
    def save_solution(self):
        # Append the solution to solutions.txt
        with open('solutions.txt', 'a') as f:
            print('Saved current solution to solutions.txt')
            solution = str(self.grid)
            f.write(solution + '\n')
            # exit
            sys.exit()
            # Set solved back to False after saving
            #self.solved = False