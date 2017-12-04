import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
N = 100
ON = 255
OFF = 0
vals = [ON, OFF]
class Board(object):
    def __init__(self,size=(N,N),cur_matrix=np.zeros((N,N))):
        self.size=size
        self.cur_matrix=cur_matrix
        self.next_matrix=np.zeros(size)

    def load_matrix(self,matrix):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.cur_matrix[row][col]=matrix[row][col]

    def update_next_matrix(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                neighbors_amount=0
                for ri in range(-1,2):
                    for ci in range(-1,2):
                        # if 0<=row+ri<self.size[0] and 0<=col+ci<self.size[1] and (ri!=0 or ci!=0):
                        neighbors_amount+=self.cur_matrix[(row+ri)%N][(col+ci)%N]/ON
                self.update_entity(row,col,neighbors_amount)

    def update_entity(self,row,col,amount):
        status=self.cur_matrix[row][col]
        if status==1:
            if amount <2:
                self.next_matrix[row][col]=0
                return
            if amount>3:
                self.next_matrix[row][col]=0
                return
        else:
            if amount==3:
                self.next_matrix[row][col] = 1


    def advance_stage(self):

        self.update_next_matrix()
        self.cur_matrix=self.next_matrix
        return self.cur_matrix




b=Board(np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N))
print b.cur_matrix
fig, ax = plt.subplots()
#plt.imshow(b.cur_matrix)
ax.matshow(size=(N,N),cur_matrix=b.cur_matrix)
plt.figure()
fig, ax = plt.subplots()
mat = ax.matshow(b.cur_matrix)
def animate(data):
    global b
    newGrid=b.advance_stage()
    #print newGrid
    mat.set_data(newGrid)
    return [mat]

ani = animation.FuncAnimation(fig, animate, interval=50, blit=True)
plt.show()
print "hi"
