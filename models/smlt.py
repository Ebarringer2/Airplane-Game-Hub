# training for the ml algorithm
from models.sml import SML
from models.sudoku.sudoku_class import Sudoku
class SMLT(Sudoku):
    def __init__(self, data_file : str, sml : SML, window):
        '''
        data file is the file containing the training data
        i.e. 'solutions.txt'
        '''
        self.running = False 
        self.training = False
        self.data_file = data_file
        self.SML = sml
        self.window = window
        self.sudoku = Sudoku(self.window)
        self.raw_data : list[tuple[str, str]] = []
    def run(self, epochs : int, g_iterations : int):
        '''
        *Args
            *epochs --> number of training loops
            *g_iterations --> amount of training data, number of times that the 
            sudoku instance generates and solves a sudoku board
        '''
        self.running = True 
        print("Running: " + str(self.running))
        for epoch in range(1, epochs):
            print(f'Epoch {epoch}: generating raw data: sudoku grid')
            self.sudoku.train_generate(iterations=g_iterations)
            print(f'Epoch {epoch}: formatting unsolved and solved grid to tuple')
            self.sudoku.process_raw_data()
            self.raw_data = self.sudoku.RAW_DATA
            print(f'Epoch {epoch}: updating raw data')
            self.SML.raw_data = self.raw_data
            print(f'Epoch {epoch} raw data: {self.SML.raw_data}')
            print(f'Epoch {epoch}: Preprocessing data')
            train_data = self.SML.preprocess_data()
            print(f'Epoch {epoch}: training')
            self.training = True 
            self.SML.train(train_data)
            print(f'Epoch {epoch} result: ')
    '''
    method for fetching raw data from the text file **NOT PREPROCESSED
    formats the data from the .txt file into a tuple readable by the SML
    updates self.raw_data to the data pulled from the text file
    not necessary --> alternative is to fetch the raw data directly from the sudoku
    instance, but it can be handy sometimes
    '''
    def fetch(self):
        with open(self.data_file, 'r') as df:
            data = df.readlines()
        raw_data : list[tuple[str]] = []
        for line in data:
            unsolved = ''
            solution = ''
            pair : tuple = ()
            if data.index(line) == 0:
                unsolved = line
            elif data.index(line) % 2 == 0:
                solution = line 
            elif data.index(line) % 2 > 0:
                unsolved = line 
            pair += (unsolved, solution)
            raw_data.append(pair)
        self.raw_data = raw_data
    def generate_loop(self, iterations : int):
        for i in range(1, iterations):
            self.SML.sudoku.generate_sudoku()