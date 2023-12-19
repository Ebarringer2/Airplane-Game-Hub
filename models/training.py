# training for the ml algorithm
from models.sudoku.sudoku_class import Sudoku 
from models.sudoku import SML
class MLT(Sudoku):
    def __init__(self, data_file : str, sml : SML):
        '''
        data file is the file containing the training data
        i.e. 'solutions.txt'
        '''
        self.running = False 
        self.training = False
        self.data_file = data_file
        self.SML = sml
    def run(self):
        self.running = True 
        self.generate_sudoku()
        self.fetch()
    def fetch(self):
        unsolved = ''
        solution = ''
        training_pair : list[list[str]] = []
        with open(self.data_file, 'r') as df:
            data = df.readlines()
            for line in data:
                if data.index(line) == 0:
                    unsolved = line
                elif data.index % 2 == 0:
                    solution = line 
                elif data.index % 2 > 0:
                    unsolved = line 
