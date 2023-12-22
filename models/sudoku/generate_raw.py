from random import randint as r

class Generator:
    def __init__(self, iterations : int, X_train_path : str, y_train_path : str):
        self.iterations = iterations 
        '''self.base_grid : list[list[int]] = [
		    [7, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 8, 0, 0, 1, 0, 0],
		    [0, 2, 0, 0, 0, 0, 0, 0, 9],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 6, 0, 0, 0],
		    [0, 3, 0, 0, 8, 0, 0, 6, 0],
		    [0, 0, 0, 0, 0, 0, 0, 0, 0],
		    [0, 0, 4, 0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0, 0, 5, 0]
	    ]'''
        self.base_grid : list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]
        self.X_train_path = X_train_path
        self.y_train_path = y_train_path
    def generate(self):
        for iteration in range(1, self.iterations):
            print(f'Iteration {iteration} : Generating Sudoku Board')
            self.printgap()
            board : [list[list[int]]] = [[0 for _ in range(9)] for _ in range(9)]
            print('EMPTY BOARD')
            print(str(board))
            self.printgap()
            for i in range(9):
                for j in range(9):
                    board[i][j] = self.base_grid[i][j]
            print('COPIED BOARD') 
            print(str(board))
            self.printgap()
            for i in range(9):
                for j in range(9):
                    board = self.solve(board, i, j)
            print('SOLVED BOARD')
            print(board)
            self.printgap()
            for _ in range(r(5, 10)):
                row, col = r(0, 8), r(0, 8)
                board[row][col] = 0
            self.update_X(board)
    def solve(self, board : list[list[int]], i : int, j : int) -> list[list[int]]:
        '''empty_cell = self.find_empty(board) 
        if not empty_cell:
            self.update_y(board)
            return board 
        row, col = empty_cell 
        for num in range(1, 10):
            if self.valid(board, row, col, num):
                board[row][col] = num 
                if self.solve(board):
                    self.update_y(board)
                    return board 
                board[row][col] = 0 
        raise ValueError(f'inputted board {str(board)} has no solution')'''
        while board[i][j] != 0:
            if i < 8:
                i += 1
            elif i == 8 and j < 8:
                i = 0
                j += 1
            elif i == 8 and j == 8:
                return board
            for it in range(1, 10):
                if self.valid(board, i, j, it):
                    board[i][j] = it 
                    if self.solve(board, i, j) == 1:
                        return board 
                    else:
                        board[i][j] = 0
        print('NO SOLUTION')
        self.printgap() 
        return board
    def find_empty(self, board : list[list[int]]):
        for idx in range(81):
            i, j = divmod(idx, 9)
            if board[i][j] == 0:
                return (i, j)
        return None 
    def valid(self, board : list[list[int]], row : int, col: int, num : int) -> bool:
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False 
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False 
        return True
    def update_y(self, board : list[list[int]]) -> None:
        with open(self.y_train_path, 'a+') as f:
            string : str = ''
            for idx in range(81):
                i, j = divmod(idx, 9)
                it = board[i][j]
                string += str(it)
            f.write(string)
            f.write('\n')
    def update_X(self, board : list[list[int]]) -> None:
        with open(self.X_train_path, 'a+') as f:
            string : str = ''
            for idx in range(81):
                i, j = divmod(idx, 9)
                it = board[i][j]
                string += str(it)
            f.write(string)
            f.write('\n')
    def printgap(self):
        print('\n')
        print('-----------------------------------------------------------------------')
        print('\n')