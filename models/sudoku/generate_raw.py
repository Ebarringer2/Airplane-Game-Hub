class Generator:
    def __init__(self, iterations : int):
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
    def generate(self):
        for iteration in self.iterations:
            print(f'Iteration {iteration} : Generating Sudoku Board')
            