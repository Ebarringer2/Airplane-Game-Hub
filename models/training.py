# training for the ml algorithm
from models.sudoku.sudoku_class import Sudoku 
from models.sudoku import SML
class MLT(Sudoku):
    def __init__(self, data_file : str):
        '''
        data file is the file containing the training data
        i.e. 'solutions.txt'
        '''
        self.running = False 
        self.training = False
        self.data_file = data_file
    def run(self):
        self.running = True 
        self.generate_sudoku()
        self.fetch()
    def fetch(self):
        with open(self.data_file, 'r') as df:
            data = df.read()
