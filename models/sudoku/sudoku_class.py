# some code used from https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/

import sys
import pygame
from random import randint
from typing import List
from game.sudoku.dancing_links import SudokuSolver, DancingLinks
import threading 

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
        self.unsolved_board = []
        self.board_string = ''
		# init pygame bases
        pygame.font.init()
        self.font1 = pygame.font.SysFont('arial', 18)
        self.window = window
        # for the dancing links solver
        self.DANCINGLINKS = None
        # for the sudoku solver object
        self.SUDOKUSOLVER = None
        # init with sample board
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
        # for machine learning
        self.training = False
        self.RAW_DATA : list[tuple[str, str]] = []
        self.list_unsolved_strs : list[str] = []
        self.list_solved_strs : list[str] = []
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
        # update for later method analysis 
        self.grid = board
        self.unsolved_board = board
        print(self.grid)
        print('\n')
        print(self.unsolved_board)
        string = ''
        for i in range(9):
            for j in range(9):
                it = self.unsolved_board[i][j]
                self.board_string += str(it)
        print('String of unsolved board: ' + self.board_string)
        # CREATE STRING
        # for i in range(9):
        #     for j in range(9):
        #         self.checker.append(self.unsolved_board[i][j])
        #         print()
        with open('./solutions.txt', 'a+') as f:
            for i in range(9):
                for j in range(9): 
                    it = str(self.unsolved_board[i][j])
                    f.write(it)
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
    # threaded method
    def solve_puzzle_thread(self):
        if self.generated:
            self.check_solved()
        if self.solved:
            self.save_solution()
        if self.flag2 == 1:
            if self.solve(0, 0) == False:
                self.error = 1
            else:
                self.rs = 1
    # run loop
    def run(self):
        self.running = True
        print(self.running)
        self.generate_sudoku()
        # create a thread for solving the puzzle
        solve_thread = threading.Thread(target=self.solve_puzzle_thread)
        solve_thread.start()
        while self.running:
            # white background
            self.screen.fill((255, 255, 255))
            # update in run loop
            self.update()
    # save past solutions so that we can save time solving
    def save_solution(self) -> None:
        '''
        this method creates a dictionary in the solutions.txt file
        the dictionary is structured as follows

        <unsolved board as a string> : <solved board as a string>
        
        doing this allows the algorithm to read from this text file and 
        check whether or ot the current board has already been solved, 
        and if it has, the solution for that board can be fetched

        this allows the algorithm to save computation time. The backtracking
        solving method can be slow and tedious, so fetching past solutions is 
        very helpful
        '''
        # Append the solution to solutions.txt
        # iterate through the unsolved board
        # and the solved board and add them to the file
        with open('solutions.txt', 'a+') as f:
            # instantiate empty list to represent the unsolved board
            unsolved_board = []
            # insantiate empty list to represent the solved board
            solved_board= []
            for i in range(9):
                for j in range(9):
                    it_unsolved = self.unsolved_board[i][j]
                    str_it_unsolved = str(it_unsolved)
                    unsolved_board.append(str_it_unsolved)
                    it_solved = self.grid[i][j]
                    str_it_solved = str(it_solved)
                    solved_board.append(str_it_solved)
            # add the unsolved board to the dictionary pairing in the txt file
            #for i in unsolved_board:
            #    f.write(str(i))
            # add the colon for parsing the dictionary
            f.write('\n')
            # add the solved board to the dictionary pairing
            for i in solved_board:
                f.write(str(i))
            #f.write(unsolved_board + ' : ' + solved_board)
            f.write('\n') # new line after printing the dictionary entry
            print('Saved current solution to solutions.txt')
            # exit
            self.check_solutions()
            sys.exit()
            # Set solved back to False after saving
            #self.solved = False
    # method for scanning the solutions dictionary for saving computation time
    def check_solutions(self):
        # initiate empty unsolved board list
        unsolved_boards = []
        # initiate empty solutions list
        sols = []
        with open('solutions.txt', 'r') as f:
            # get the solutions by reading the txt line by line
            dictionary = f.readlines()
            l = len(dictionary)
            print('Num solutions: ' + str(l))   # for debugging
            '''
            iterate through all of the solutions by new line character
            split all of the dictionary pairings by the colon divider
            '''
            '''for pairing in dictionary:
                split = (pairing.split(' : '))
                print(split)
                # append the unsolved board to the list
                unsolved_boards.append(split[0])
                # grab the solution by avoiding index out of range error
                reversed_dict = split.reverse()
                print(reversed_dict)
                solution = reversed_dict - ' : ' - split[0]
                print(solution)
                #print('Solution: ' + str(sol[0]))'''
            for i in range(0, l - 1):
                val = dictionary[i]
                if i % 2 != 0:
                    print('Solution ' + str(i - 1) + ' ' + str(val))
                else:
                    print('Unsolved Board ' + str(i) + ' ' + str(val))
                '''
                now we can scan the past unsolved boards, check
                if thecurrent board matches any of them,
                and if they do, we can use the past solution to skip the process of 
                backtrack algorithm solving, which saves computation time
                '''
            # define empty string
            # iterate through all of the values in the solution string
            if self.board_string == val:
                print('THIS BOARD HAS EXISTED IN THE PAST')
    # method for solving using the dancing links algorithm
    def solver_run(self):
        '''
        this run loop is largely similar to the normal run loop for this class.
        the main difference is the addition of the dancing links and sudoku solving algorithm
        written in dancing_links.py to solve the board. Again, the main goal here is to decrease 
        computation difficult and time, increasing performance, so if this algorithm ends up to be slower
        on the run device than the previous backtracking algorithm, one is able to use the other run loop
        defined to still use that algorithm. This addition might just be faster than that backtracking 
        algorithm, so that is why I am including it
        '''
        self.running = True 
        self.DANCINGLINKS = DancingLinks(self.grid)
        self.SUDOKUSOLVER = SudokuSolver()
        while self.running:
            self.screen.fill((255, 255, 255))
            '''
            dont display in this run loop so that pygame being incompetent
            doesn't crash the dancing links algorithm
            dont update in this run loop so that pygame being incompetent
            doesn't crash the dancing links algorithm
            '''
            #self.update()
            #pygame.display.update()
            # iterate through events in the pygame cache like the previous run loop
            for event in pygame.event.get():
                # exit method
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print('terminating program')
                    sys.exit('terminated')
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    print('solving grid using dancing links')
                    # check if the board is solved
                    if self.DANCINGLINKS.solve():
                        print('solution found')
                        self.grid = self.SUDOKUSOLVER.extract_solution(self.DANCINGLINKS.solution)
    '''
    methods oriented around properly generating
    basically just refactored generation and solving
    that maximizes processing efficiency by neglecting
    all pygame updated

    this is just for training, when one wants to access the
    actual game, one should use the typical generation and solving 
    methods for one's game 
    '''
    def train_generate(self, iterations : int):
        print('generating train data')
        for i in range(1, iterations):
            unsolved_string = ''
            solved_string = ''
            board = [[0 for _ in range(9)] for _ in range(9)]
            for i in range(9):
                for j in range(9):
                    board[i][j] = self.grid[i][j]
            for i in range(9):
                for j in range(9):
                    solved_board = self.train_solve(i, j, board)
            for i in range(9):
                for j in range(9):
                    board[i][j] = solved_board[i][j]
            for n in range(9):
                for k in range(9):
                    it = str(board[n][k])
                    solved_string += it
                    print(solved_string) 
            for _ in range(randint(10, 20)):
                row, col = randint(0, 8), randint(0, 8)
                board[row][col] = 0
            for i in range(9):
                for j in range(9):
                    iterator = str(board[i][j])
                    unsolved_string += iterator
            with open('./models/X_train.txt', 'a+') as f:
                f.write(unsolved_string)
                f.write('\n')
                print('wrote generated board to X_train.txt')
            self.list_unsolved_strs.append(unsolved_string)
            with open('./models/y_train.txt', 'a+') as f:
                f.write(solved_string)
                f.write('\n')
                print('wrote solved board to y_train.txt')

    def train_solve(self, i : int, j : int, board : list[list[int]]) -> list[list[int]]:
        while board[i][j] != 0:
            if i < 8:
                i += 1
            elif i == 8 and j < 8:
                i = 0
                j += 1
            elif i == 8 and j == 8:
                return board
        for it in range(1, 10):
            if self.is_valid(i, j, it):
                board[i][j] = it
                if self.train_solve(i, j, board) == board:
                    return board 
                else:
                    board[i][j] = 0
        '''for i in range(9):
            for j in range(9):
                iterator = str(board[i][j])
                solved_string += iterator 
        with open('./models/y_train.txt', 'a+') as f:
            f.write(solved_string)
            f.write('\n')
            print('wrote solved board to y_train.txt')
        self.list_solved_strs.append(solved_string)
        print('appended solved board to solutions list')'''
    '''
    method to format the raw data into a data structure that the SML and 
    SMLT can proprocess
    '''
    def process_raw_data(self):
        for unsolved, solved in zip(self.list_unsolved_strs, self.list_solved_strs):
            t : tuple = (unsolved, solved)
            self.RAW_DATA.append(t)