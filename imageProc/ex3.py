import numpy as np

def create_gaussian_filter(size):
    if (size<2):
        print "that is going to be a problem"
        return False
    base=[1,1]
    gFilter=[1,1]
    for i in range(2,size):
        gFilter=np.convolve(gFilter,base)
    gFilter=gFilter/float(np.sum(gFilter))
    return gFilter

def create_2d_filter(filter):
    hx=np.array([filter])
    #print hx
    hy=hx.transpose()
    #print hy
    return np.dot(hy,hx)


def create_average_filter(size):
    if size<0:
        print "not gonna happen"
        return False
    aFilter= np.ones(size)
    aFilter=aFilter/np.sum(aFilter)
    return aFilter


gFilter1D = create_gaussian_filter(5)
gFilter2D= create_2d_filter(gFilter1D)
aFilter2D= create_average_filter((5,5))

print gFilter2D
print aFilter2D