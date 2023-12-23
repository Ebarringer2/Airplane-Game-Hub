from models.sudoku.generate_raw import Generator

for i in range(0, 100):
    for j in range(0, 4):
        g = Generator(
            iterations=51,
            X_train_path='./xtrain.txt',
            y_train_path='./ytrain.txt',
            base_grid_select=j
        )
        print(str(g.base_grid))
        print(f'GENERATOR {j}')
        g.generate()