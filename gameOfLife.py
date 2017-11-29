import numpy as np
import matplotlib.pyplot as plt


class Entity(object):
    def __init__(self, status=0):
        self.status=status
        self.neighbours = []


class Board(object):
    def __init__(self,size=(10,10)):
        self.size=size
        self.matrix=np.empty(size,dtype=Entity)
        self.create_matrix()

    def create_matrix(self):
        for row in range(self.size[0]):
            for col in range (self.size[1]):
                self.matrix[row][col]=Entity()

    def load_matrix(self,matrix):
        i

    def advance_step(self):
        for row in range(self.size[0]):
            for col in range (self.size[1]):
                pass



b=Board()
print(b.matrix[0][0].status)
