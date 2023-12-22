from random import randint as r

class Generator:
    def __init__(self, iterations : int, X_train_path : str, y_train_path : str):
        self.iterations = iterations 
        self.base_grid : list[list[int]] = [
            [0, 0, 0, 6, 9, 0, 0, 1, 7],
            [8, 0, 1, 3, 0, 0, 4, 0, 0],
            [9, 3, 0, 1, 0, 4, 0, 8, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0],
            [5, 0, 9, 8, 7, 2, 6, 0, 1],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 7, 0, 5, 0, 9, 0, 4, 3],
            [0, 0, 8, 0, 0, 3, 1, 0, 9],
            [3, 9, 0, 0, 6, 1, 0, 0, 0]
        ]
        self.X_train_path = X_train_path
        self.y_train_path = y_train_path
    def generate(self):
        for iteration in self.iterations:
            print(f'Iteration {iteration} : Generating Sudoku Board')
            board : [list[list[int]]] = [[0 for _ in range(9)] for _ in range(9)]
            for idx in range(81):
                i, j = divmod(idx, 9)
                board[i][j] = self.base_grid[i][j] 
            board = self.solve(board)
            for _ in range(r(5, 10)):
                row, col = r(0, 8), r(0, 8)
                board[row][col] = 0
            self.update_X(board)
    def solve(self, board : list[list[int]]) -> list[list[int]]:
        empty_cell = self.find_empty(board) 
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
        ValueError(f'inputted board {str(board)} has no solution')
        return None
    def find_empty(self, board : list[list][int]) -> tuple(int, int):
        for idx in range(81):
            i, j = divmod(idx, 9)
            if board[i][j] == 0:
                return (i, j)
        return None 
    def valid(self, board : list[list[int]], row : int, col: int, num : int) -> bool:
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False 
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for idx in range(9):
            i, j = divmod(idx, 3)
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