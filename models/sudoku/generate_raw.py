from random import randint as r

class Generator:
    def __init__(self, iterations : int, X_train_path : str, y_train_path : str, base_grid_select : int):
        '''
        base_grid_select starts at 0, indexing the sudoku puzzles 
        '''
        self.iterations = iterations 
        '''sudoku_puzzles : list[list[list[int]]] = [
            [
                [0, 0, 0, 2, 0, 0, 0, 6, 0],
                [0, 0, 9, 0, 0, 1, 0, 0, 8],
                [6, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 8, 0, 0, 0, 0, 0, 2, 0],
                [4, 0, 0, 8, 0, 5, 0, 0, 6],
                [0, 2, 0, 0, 0, 0, 0, 7, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 7],
                [9, 0, 0, 4, 0, 0, 6, 0, 0],
                [2, 0, 0, 0, 0, 8, 0, 5, 4]
            ],
            [
                [0, 0, 0, 0, 0, 3, 0, 0, 8],
                [0, 0, 0, 9, 0, 0, 0, 7, 0],
                [0, 0, 7, 0, 0, 0, 0, 4, 0],
                [1, 0, 0, 4, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 0, 0, 0, 9, 0],
                [0, 0, 2, 0, 0, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 8, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 5, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 6]
            ],
            [
                [0, 9, 0, 7, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 6, 0],
                [0, 0, 0, 8, 0, 0, 0, 0, 0],
                [0, 0, 0, 9, 0, 0, 0, 7, 2],
                [7, 0, 0, 0, 0, 0, 0, 0, 4],
                [0, 2, 0, 0, 0, 0, 0, 0, 8],
                [0, 0, 0, 0, 0, 2, 0, 0, 0],
                [0, 5, 0, 0, 0, 0, 9, 0, 0],
                [0, 0, 6, 0, 0, 3, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0, 0, 4, 3, 0, 0],
                [0, 6, 3, 0, 0, 0, 9, 2, 0],
                [0, 0, 0, 0, 9, 0, 0, 1, 8],
                [0, 0, 0, 6, 1, 0, 0, 0, 7],
                [0, 8, 0, 0, 0, 0, 0, 3, 0],
                [7, 0, 0, 0, 5, 3, 0, 0, 0],
                [2, 4, 0, 0, 8, 0, 0, 0, 0],
                [0, 7, 1, 0, 0, 0, 4, 6, 0],
                [0, 0, 8, 1, 0, 0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 5, 0, 0, 0, 0, 0],
                [0, 0, 0, 9, 3, 0, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 8, 0, 7],
                [0, 0, 5, 3, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [0, 2, 1, 0, 0, 0, 0, 0, 9],
                [4, 0, 7, 0, 0, 6, 0, 0, 0],
                [0, 8, 0, 0, 7, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 2, 1, 0]
            ],
        ]
        self.base_grid = sudoku_puzzles[base_grid_select]'''
        grid1 = [
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
        grid2 = [
                [0, 0, 0, 0, 0, 3, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 8, 2, 0, 0, 0, 7, 0],
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 8, 0, 0],
                [0, 0, 0, 0, 7, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 7, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 8, 0, 0, 0, 0, 0]
            ]
        if base_grid_select == 0:
            self.base_grid : list[list[int]] = grid1
        elif base_grid_select == 1:
            self.base_grid : list[list[int]] = grid2
        elif base_grid_select == 2:
            reversed = grid1[::-1]
            full_reversed = [inner_list[::-1] for inner_list in reversed]
            self.base_grid : list[list[int]] = full_reversed
        elif base_grid_select == 3:
            reversed = grid2[::-1]
            full_reversed = [inner_list[::-1] for inner_list in reversed]
            self.base_grid : list[list[int]] = full_reversed
        else:
            self.base_grid : list[list[int]] = grid1
        #self.base_grid : list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]
        self.X_train_path = X_train_path
        self.y_train_path = y_train_path
        self.x_updated : bool = False 
        self.y_updated : bool = False
    def generate(self):
        for iteration in range(1, self.iterations):
            unsolved_board : list[list[int]] = []
            solved_board : list[list[int]] = []
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
                    self.solve(board, i, j)
            solved_board = board
            self.update_y(solved_board)
            print('SOLVED BOARD')
            print(board)
            self.printgap()
            for _ in range(r(10, 15)):
                row, col = r(0, 8), r(0, 8)
                board[row][col] = 0
            unsolved_board = board
            self.update_X(unsolved_board)
    def solve(self, board : list[list[int]], i : int, j : int) -> bool:
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
                return True
            for it in range(1, 10):
                if self.valid(board, i, j, it):
                    board[i][j] = it 
                    if self.solve(board, i, j):
                        return True
                    else:
                        board[i][j] = 0
        return False
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
        i, j = self.find_empty(board)
        if board[i][j] == 0:
            self.printgap()
            print('SOLUTION CONTAINS ZEROES')
            self.printgap()
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