import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

import random

a = np.arange(54).reshape(18, 3)
b = np.arange(54).reshape(3, 18)
# print a
# print b
c = np.dot(a, b)
# print c
d = np.diag(c)
print "\n\n\n\n exercise1 answer:\n{}".format(d)
a = np.arange(5) + 1
# print a
b = np.zeros(len(a) * 4)
b[::4] = a
print "exercise2 answer:\n{}".format(b)
array = np.array([7, 23, 56, 875, 24, 65, 87, 123, 65, 7, 25, 135])
window = 4
print array
array2 = np.concatenate((array, np.zeros(window)))
averaged = [sum(array2[i:i + window]) / window for i in range(len(array2) - window)]

print "exercise3 answer:\n{}".format(averaged)


# exercise 4:
class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def distance(P1, P2, p):
    distances = []
    for p1, p2 in zip(P1, P2):
        if (p1.x != p2.x or p1.y != p2.y):
            distance = abs((p2.y - p1.y) * p.x - (p2.x - p1.x) * p.y + p2.x * p1.y - p2.y * p1.x) / math.sqrt(
                (p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)
        else:
            distance = math.sqrt((p.x - p1.x) ** 2 + (p.y - p1.y) ** 2)
        distances.append(distance)

    return distances


p = Point(1, 2)
P1 = [Point(0, 0), Point(3, 6), Point(3, 6)]
P2 = [Point(0, 3), Point(5, 7), Point(3, 4)]
print "exercise 4:\n{}".format(distance(P1, P2, p))

# exercise 5:
a = np.arange(9).reshape(3, 3)
print "exercise 5:\n{}".format((np.linalg.matrix_rank(a)))

# exercise 6:
a = np.array([1, 54, 3, 3478, 5, 1, 2, 5, 6, 73, 2, 1])
print a
counts = np.bincount(a)
print counts

print "exercise 6:\n{}".format(np.argmax(counts))

# exercise 7:
# a = []
# a.append(np.arange(16).reshape(4, 4))
# a.append()
#
# b = np.arange(4)

a = [np.arange(16).reshape(4, 4), np.arange(16, 32).reshape(4, 4), np.arange(32, 48).reshape(4, 4)]
# print a[0]
# print a[1]
b = [np.arange(4), np.arange(4, 8), np.arange(8, 12)]
c = [np.dot(x, y) for x, y in zip(a, b)]
print "exercise 7:\n{}".format(sum(c))
cona = reduce(lambda x, y: np.concatenate((x, y), 1), a)
conb = reduce(lambda x, y: np.concatenate((x, y), 0), b)
print cona
print conb
ans = np.dot(cona, conb)
print "Lee asa et ze ! exercise 7:\n{}".format(ans)
# exercise 8:
t = np.arange(1, 10, 0.01)
x = [math.sin(b) + math.sin(100 * b) for b in t]
y = np.fft.fft(x)
plt.plot(t, x)
plt.plot(t, y)
