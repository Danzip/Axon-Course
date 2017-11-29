import numpy as np
import matplotlib.pyplot as plt


class Entity(object):
    def __init__(self, status=0):
        self.status=status
        self.neighbours_amount=0


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
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.matrix[row][col].status=matrix[row][col]
        #pass


    def update_neighbor_amount(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                neighbors_amount=0
                for ri in range(-1,2):
                    for ci in range(-1,2):
                        if 0<=row+ri<=self.size[0] and 0<=col+ci<=self.size[1] and (ri!=0 or ci!=0):
                            neighbors_amount+=self.matrix[row+ri][col+ci].status
                self.matrix[row][col]=neighbors_amount

    def update_board(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                amount=self.matrix[row][col].neighbours_amount
                status=self.matrix[row][col].status
                if status==1:
                    if amount <2:
                        self.matrix[row][col].status=0
                        continue
                    if amount>3:
                        self.matrix[row][col].status = 0
                        continue
                else:
                    if amount==3:
                        self.matrix[row][col].status = 1








b=Board()
print(b.matrix[0][0].status)