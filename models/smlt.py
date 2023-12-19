# training for the ml algorithm
from models.sudoku.sudoku_class import Sudoku 
from models.sml import SML
class SMLT():
    def __init__(self, data_file : str, sml : SML):
        '''
        data file is the file containing the training data
        i.e. 'solutions.txt'
        '''
        self.running = False 
        self.training = False
        self.data_file = data_file
        self.SML = sml
        self.raw_data : list[tuple[str]] = []
    def run(self, epochs : int):
        self.running = True 
        print("Running: " + self.running)
        for epoch in epochs:
            print(f'Epoch {epoch}: generating raw data: sudoku grid')
            self.SML.sudoku.generate_sudoku()
            print(f'Epoch {epoch}: fetching data from text file')
            self.fetch()
            print(f'Epoch {epoch}: updating raw data')
            self.SML.raw_data = self.raw_data
            print(f'Epoch {epoch}: Preprocessing data')
            train_data = self.SML.preprocess_data()
            print(f'Epoch {epoch}: training')
            self.training = True 
            self.SML.train(train_data)
            print(f'Epoch {epoch} result: ')
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