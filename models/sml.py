import numpy as np 
import tensorflow as tf 
from tensorflow.python.keras.models import Sequential 
from tensorflow.python.keras.layers import Dense, Flatten, Reshape 
from tensorflow.python.keras.optimizers import adam_v2
from tensorflow.python.keras.losses import SparseCategoricalCrossentropy 

def to_categorical(y, num_classes=None, dtype='float32'):
    '''
    converts a class vector (integers) to binary class matrix
    '''
    y = np.asarray(y, dtype='int')
    if num_classes is None:
        num_classes = np.max(y) + 1
    if y.ndim > 1:
        raise ValueError('to_categorical expects 1d array, got ndim={}'.format(y.ndim))
    n = y.shape[0]
    categorical = np.zeros((n, num_classes), dtype=dtype)
    categorical[np.arange(n), y] = 1
    return categorical

class SML:
    def __init__(self, unsolved_board : list[list[int]]):
        self.model = self.build_model() 
        print('compiled SML model')
        self.initial_grid = unsolved_board
        self.raw_data : list[tuple[str]] = [
            ()
        ]
        self.processed_data : list[tuple[str]] = [
            ()
        ]
        self.solution : str = None
    def build_model(self):
        model = Sequential([
            Flatten(input_shape=(81,)),
            Dense(128, activation='relu'),
            Dense(81, activation='softmax'),
            Reshape((9, 9))
        ]) 
        model.compile(optimizer=adam_v2.Adam(), loss=SparseCategoricalCrossentropy, metrics=['accuracy'])
        return model 
    def train(self, X_train, y_train, epochs):
        self.model.fit(X_train, y_train, epochs, batch_size=32) 
    def generate(self):
        sudoku_grid = np.zeros((9, 9), dtype=int)
        for i in range(9):
            for j in range(9):
                sudoku_grid[i, j] = self.initial_grid[i][j] 
        while True:
            flat_grid = sudoku_grid.flatten()
            predictions = self.model.predict(flat_grid.reshape(1, -1))
            predicted_values = np.argmax(predictions, axis=-1).reshape((9, 9))
            sudoku_grid[predicted_values == 1] = flat_grid[predicted_values == 1]
            if np.all(sudoku_grid != 0):
                break 
        return sudoku_grid
    def solve(self, puzzle_str):
        puzzle = np.array([int(char) for char in puzzle_str])
        puzzle_flat = puzzle.reshape(1, 81)
        predictions = self.model.predict(puzzle_flat)
        solution = np.argmax(predictions, axis=-1)
        self.solution = solution.reshape((9, 9))
    def preprocess_data(self):
        X_train = []
        y_train = []
        for sudoku_str, solution_str, in self.raw_data:
            # convert strings to numpy arrays
            sudoku_grid = np.array([int(char) for char in sudoku_str])
            solution_grid = np.array([int(char) for char in solution_str])
            # flatten arrays
            sudoku_flat = sudoku_grid / 9.0
            solution_flat = solution_grid / 9.0 
            # one-hot encode the solution
            solution_onehot = to_categorical(solution_flat, num_classes=10)
            # append to the training data
            X_train.append(sudoku_flat)
            y_train.append(solution_onehot.flatten())
        return np.array(X_train), np.array(y_train)