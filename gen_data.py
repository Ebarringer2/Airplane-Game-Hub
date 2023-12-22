from models.sudoku.generate_raw import Generator
generator = Generator(
    iterations=100,
    X_train_path='./xtrain.txt',
    y_train_path='./ytrain.txt'
    )
generator.generate()