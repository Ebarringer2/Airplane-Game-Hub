import tensorflow as tf
import numpy as np

# Define the Sudoku puzzle (0 represents empty cells)
sudoku_puzzle = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Convert the puzzle to a one-hot encoded format
def puzzle_to_onehot(puzzle):
    onehot = np.zeros((9, 9, 9))
    for i in range(9):
        for j in range(9):
            if puzzle[i, j] != 0:
                onehot[i, j, puzzle[i, j] - 1] = 1
    return onehot

# Create the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(9, 9, 9)),
    #tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(9, activation='softmax'),
    tf.keras.layers.Reshape((9, 9, 9))
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
onehot_puzzle = puzzle_to_onehot(sudoku_puzzle)
labels = sudoku_puzzle.reshape((9, 9, 1)) - 1  # Subtract 1 to convert to 0-indexed labels
nonzero_indices = labels != -1
labels_onehot = tf.keras.utils.to_categorical(labels[nonzero_indices], num_classes=9)
model.fit(onehot_puzzle.reshape((1, 9, 9, 9))[..., :9], labels_onehot.reshape((1, np.sum(nonzero_indices), 9, 1)), epochs=10)

# Solve a Sudoku puzzle
def solve_sudoku(puzzle, model):
    onehot_puzzle = puzzle_to_onehot(puzzle)
    predicted_labels = model.predict(onehot_puzzle.reshape((1, 9, 9, 9)))
    predicted_labels = np.argmax(predicted_labels, axis=-1) + 1  # Add 1 to convert back to 1-indexed labels
    solved_puzzle = np.where(puzzle == 0, predicted_labels[0], puzzle)
    return solved_puzzle

# Print the solved Sudoku puzzle
solved_puzzle = solve_sudoku(sudoku_puzzle, model)
print("Original Sudoku Puzzle:")
print(sudoku_puzzle)
print("\nSolved Sudoku Puzzle:")
print(solved_puzzle)
