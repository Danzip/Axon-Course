################################################################################
# conway.py
#
# Author: electronut.in
#
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 1
OFF = 0
vals = [ON, OFF]

class Board(object):
    def __init__(self,grid=np.zeros((N,N)),newGrid=np.zeros((N,N))):
        self.grid=grid
        self.newGrid=newGrid

    def calculate_state(self,i,j):
        # compute 8-neghbor sum
        # using toroidal boundary conditions - x and y wrap around
        # so that the simulaton takes place on a toroidal surface.
        total=0
        for r in range(-1,2):
            for c in range(-1,2):
                if(r!=0 or c!=0):
                    total += (self.grid[(i+r)%N, (j+c) % N])  / ON
                # apply Conway's rules
        if self.grid[i, j] == ON:
            if (total < 2) or (total > 3):
                self.newGrid[i, j] = OFF
        else:
            if total == 3:
                self.newGrid[i, j] = ON
                # update data

    def calculate_board(self):
        self.newGrid = self.grid.copy()
        for i in range(N):
            for j in range(N):
                self.calculate_state(i,j)
        return self.newGrid

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(data):
    global b
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line
    newGrid = b.calculate_board()
    im.set_data(newGrid)
    b.grid = newGrid
    return im

b=Board(grid)
# set up animation
fig = plt.figure()
im=plt.imshow(grid,cmap='gray')
#mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()