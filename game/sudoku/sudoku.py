# coding help from https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/
###### MATERIAL CHANGED #####
## removed solving algorithm in the original script
## replaced it with a dancing links algorithm implementation
## the Dancing Links paper is linked in README.md
# DLX Sudoku Class source: https://github.com/sraaphorst/dlx-python/blob/master/examples/sudoku.py

import sys
import pygame
from random import randint
import dlx
from functools import reduce
from typing import List # for type deffing 

##import utils.output

# sudoku solver using the DLX algorithm 
'''class DLXsudoku(dlx.DLX):
    def __init__(self, grid, dim=3):
        //''Create a DLX instance representing the dim^2 by dim^2 Sudoku board
        represented by grid, which is a string of length dim^4. grid represents
        the contents of the board read from left-to-right and top-to-bottom,
        with entries from {0,...,dim^2}, where 0 represents an empty space in
        the board, and {1,...,dim^2} represent filled entries.''

        # Create the columns.
        ctr = 0
        cols = []

        self.dim = dim
        self.dimsq = dim**2

        # Create the row coverage, which determines that entry j appears in row i.
        for i in range(self.dimsq):
            cols += [(('r',i,j),ctr+j-1) for j in range(1,self.dimsq+1)]
            ctr += self.dimsq

        # Create the column coverage, which determines that entry j appears in column i.
        for i in range(self.dimsq):
            cols += [(('c',i,j),ctr+j-1) for j in range(1,self.dimsq+1)]
            ctr += self.dimsq

        # Create the grid coverage, which determines that entry k appears in grid i,j.
        for i in range(dim):
            for j in range(dim):
                cols += [(('g',i,j,k),ctr+k-1) for k in range(1,self.dimsq+1)]
                ctr += self.dimsq

        # Create the entry coverage, which determines that entry i,j in the grid is occupied.
        for i in range(self.dimsq):
            cols += [(('e',i,j),ctr+j) for j in range(self.dimsq)]
            ctr += self.dimsq

        # Create a dictionary from this, which maps column name to column index.
        sdict = dict(cols)

        # Create the DLX object.
        dlx.DLX.__init__(self, [(colname[0], dlx.DLX.PRIMARY) for colname in cols])

        # Now create all possible rows.
        rowdict = {}
        self.lookupdict = {}
        for i in range(self.dimsq):
            for j in range(self.dimsq):
                for k in range(1,self.dimsq+1):
                    val =  self.appendRow([sdict[('r',i,k)], sdict[('c',j,k)], sdict[('g',i//dim,j//dim,k)], sdict[('e',i,j)]], (i,j,k))
                    rowdict[(i,j,k)] = val
                    self.lookupdict[val] = (i,j,k)

        # Now we want to process grid, which we take to be a string of length 81 representing the puzzle.
        # An entry of 0 means blank.
        for i in range(self.dimsq**2):
            if grid[i] != '0':
                self.useRow(rowdict[(i//self.dimsq,i%self.dimsq,int(grid[i]))])


    def createSolutionGrid(self, sol):
        ''Return a two dimensional grid representing the solution.''

        # We need to determine what is represented by each row. This is easily accessed by rowname.
        solgrid = [['0']*self.dimsq for i in range(self.dimsq)]
        for a in sol:
            i,j,k = self.N[a]
            solgrid[i][j] = k
        return solgrid


    def createSolutionGridString(self, sol):
        ''Create a string representing the solution grid in nice format.''

        grid = self.createSolutionGrid(sol)
        return reduce(lambda x,y:x+y, [reduce(lambda x,y:x+y, [str(grid[r][c]) + ('|' if c % self.dim == self.dim-1 and c != self.dimsq-1 else '') for c in range(self.dimsq)], '') + ('\n' if r != self.dimsq-1 else '') + ((('-'*self.dim + '+')*(self.dim-1) + '-'*self.dim + '\n') if r % self.dim == self.dim-1 and r != self.dimsq-1 else '') for r in range(self.dimsq)], '')
                

    def createSolutionString(self, sol):
        //Return a string representation of the solution, read from left-to-right
        and top-to-bottom.

        return reduce(lambda x,y:x+y, map(str, reduce(lambda x,y:x+y, self.createSolutionGrid(sol), [])), '')
'''

# initialise the pygame font
pygame.font.init()
font1 = pygame.font.SysFont('arial', 18)

# Total window
screen = pygame.display.set_mode((500, 600))

# Title and Icon 
pygame.display.set_caption("SUDOKU")

x = 0
y = 0
dif = 500 / 9
val = 0
num_zeros = 60
empty_grid = [
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



def is_valid(board, row, col, num):
    # Check if the number is not already present in the current row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True
### SOLVING ALGORITHM USING BACKTRACKING -- ONLY ALGO THAT ACTUALLY WORKS
def solve(grid, i, j):
	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump() 
	for it in range(1, 10):
		if is_valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			# white color background
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(50) 
	return False

def generate_sudoku():
    # Start with an empty 9x9 grid
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the grid using the solve_sudoku function
    #solve(board)
    for i in range(1, 9):
          for j in range(1, 9):
                solve(board, i, j)
          
    # Remove some digits to create the puzzle
    for _ in range(randint(90, 100)):
        row, col = randint(0, 8), randint(0, 8)
        board[row][col] = 0

    return board

grid = generate_sudoku()

def draw():
	# Draw the lines
		
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:

				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif + 15))
	# Draw lines horizontally and verticallyto form grid		 
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	

# Function to draw required lines for making Sudoku grid		 
 



'''
# usage of dlx module to solve the sudoku board using dancing links algorithm
def solve_dancing_links(board: List[List[int]]) -> List[List[int]]:
    ## implementation ex. in DLX src code
    #columns = [('a',DLX.PRIMARY), ('b',DLX.PRIMARY), ('c',DLX.PRIMARY), ('d',DLX.SECONDARY), ('e',DLX.PRIMARY)]
    # then we need to create a columns array full of empty values
    columns: List[List[str, int]] = []
    for i in range(len(empty_grid)):
        # initialize empty array
        pair = []
        # initialize str index for the column setup
        pair_index = 'c' + str(i)
        pair.append(pair_index)
        # append column positional value
        pair.append(0)
        # append the pair to the columns 2d array
        columns.append(pair)
          
    dlx_solver = dlx.DLX()
    # Create a binary matrix for the Sudoku constraints
    matrix = []
    for i in range(9):
        for j in range(9):
            for num in range(1, 10):
                row = [0] * (9 * 9 * 4)
                row[i * 9 + j] = 1
                row[9 * 9 + i * 9 + num - 1] = 1
                row[2 * 9 * 9 + j * 9 + num - 1] = 1
                row[3 * 9 * 9 + (i // 3 * 3 + j // 3) * 9 + num - 1] = 1
                matrix.append(row)
    # Set the matrix in the dlx solver
    # Solve the puzzle
    solutions = dlx_solver.solve()
    # Update the board with the solution
    if solutions:
        solution = solutions[0]
        for i, val in enumerate(solution):
            if val == 1:
                row, col, num = i // (9 * 9), (i % (9 * 9)) // 9, (i % (9 * 9)) % 9 + 1
                board[row][col] = num
'''
# implementation of the dancing links algorithm to solve the sudoku board 
# the algorithm stores 
'''
def solve_dancing_links(board):
    def cover(i, j):
        for c in range(9 * 9):
            if dl_matrix[c][j] == 1:
                column_sizes[c] -= 1

        for r in range(9 * 9):
            if dl_matrix[r][j] == 1:
                for c in range(9 * 9):
                    dl_matrix[r][c] = 0

    def uncover(i, j):
        for r in range(9 * 9):
            if dl_matrix[r][j] == 1:
                for c in range(9 * 9):
                    dl_matrix[r][c] = matrix_backup[r][c]

        for c in range(9 * 9):
            if dl_matrix[c][j] == 1:
                column_sizes[c] += 1


    def search(k):
        if k == 9 * 9:
            return True
        c = choose_column()
        cover(0, c)
        for r in range(9 * 9):
            if dl_matrix[r][c] == 1:
                solution.append(r)
                for j in range(9 * 9):
                    if dl_matrix[r][j] == 1:
                        cover(r, j)
                # Update pygame screen after each move
                update_screen(board)
                if search(k + 1):
                    return True
                solution.pop()
                for j in range(9 * 9):
                    if dl_matrix[r][j] == 1:
                        uncover(r, j)
        uncover(0, c)
        solution.clear()  # Clear solution list before backtracking
        return False

    def choose_column():
        min_size = float('inf')
        chosen_column = -1

        for j in range(9 * 4):
            if column_sizes[j] < min_size:
                min_size = column_sizes[j]
                chosen_column = j

        return chosen_column

    def update_screen(board):
        # Update pygame screen after each move
        pygame.event.pump()
        for r in solution:
            i, j, num = r // 9, r % 9, (r % (9 * 4)) + 1
            board[i][j] = num

            # White color background
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)

    dl_matrix = [[0] * (9 * 4) for _ in range(9 * 9)]
    matrix_backup = [[0] * (9 * 4) for _ in range(9 * 9)]
    column_sizes = [9] * (9 * 4)
    solution = []

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                for k in range(1, 10):
                    if k != num:
                        dl_matrix[9 * i + j][((i * 9 + j) * 4) + k - 1] = 1

    for i in range(9):
        for j in range(9):
            for num in range(1, 10):
                matrix_backup[9 * i + j][((i * 9 + j) * 4) + num - 1] = dl_matrix[9 * i + j][((i * 9 + j) * 4) + num - 1]

    search(0)


    for r in solution:
        i, j, num = r // 9, r % 9, (r % (9 * 4)) + 1
        board[i][j] = num
'''



def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

# Highlight the cell selected
def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 



# Fill value entered in cell	 
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 15, y * dif + 15)) 

# Raise error when wrong value entered
def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 

# Check if the value entered in board is valid
def valid(m, i, j, val):
	for it in range(9):
		if m[i][it]== val:
			return False
		if m[it][j]== val:
			return False
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if m[i][j]== val:
				return False
	return True

# Solves the sudoku board using Backtracking Algorithm


# Display instruction for the game
def instruction():
	text1 = font1.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
	text2 = font1.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	 
	screen.blit(text2, (20, 540))

# Display options when solved
def result():
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

def handle_input():
    # declare global vars
    global x, y, val, grid, flag1, flag2, error, rs
    # iterate through all of the users events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_BACKSPACE:  # Delete value on backspace
                val = 0
            if event.key == pygame.K_RETURN:
                flag2 = 1


# The loop thats keep the window running
while run:
	
	# White color background
	screen.fill((255, 255, 255))
	
	handle_input()

	if flag2 == 1:
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		flag2 = 0
	if val != 0:		 
		draw_val(val)
		# print(x)
		# print(y)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2() 
		val = 0
	
	if error == 1:
		raise_error1() 
	if rs == 1:
		result()	 
	draw() 
	if flag1 == 1:
		draw_box()	 
	instruction() 

	# Update window
	pygame.display.update() 

# Quit pygame window 
pygame.quit()