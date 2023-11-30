import numpy as np
import matplotlib.pyplot as plt
import json
from numpy import empty
# Load consolidation data from a JSON file

class MatrixCalculator:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.calculate_matrix()

    def load_data(self):
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
            #print(data)
            for key, value in data.items():
                setattr(self, key, value)
    
    def calculate_gamma(self,e=None,):

            

    def calculate_matrix(self):
        if self.data is None:
            self.load_data()
        '''
        a_matrix = np.array(self.rainfall)
        b_matrix = np.array(self.runoff)
        
        # Perform matrix calculations here
        result = np.dot(a_matrix, b_matrix)
        
        return result
        '''

if __name__ == "__main__":
    calculator = MatrixCalculator('consolidation_data.json')
    print(calculator.type)
