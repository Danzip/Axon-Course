import numpy as np
import cv2
import matplotlib.pyplot as plt

#s1 = open('if.txt','r').read()
s2 = file('ex2.py', 'r').read()
s1=s2

def entropy(data_str):
    data = {c:1.0*data_str.count(c)/len(data_str) for c in set(data_str)}.values()
    return -sum(data * np.log2(data))

def mutual_information(hgram):
    # code is taken from https://matthew-brett.github.io/teaching/mutual_information.html
    pxy = hgram / float(np.sum(hgram))
    px = np.sum(pxy, axis=1)  # marginal for x over y
    py = np.sum(pxy, axis=0)  # marginal for y over x
    px_py = px[:, None] * py[None, :]  # Broadcast to multiply marginals
    nzs = pxy > 0  # Only non-zero pxy values contribute to the sum
    return np.sum(pxy[nzs] * np.log(pxy[nzs] / px_py[nzs]))


all_chars = set(s1+s2)
s1_dist = {c:1.0*s1.count(c)/len(s1) for c in all_chars}
s2_dist = {c:1.0*s2.count(c)/len(s2) for c in all_chars}

print "code entropy", entropy(s2)
print "poem entropy", entropy(s1)

hist_2d, x_edges, y_edges = np.histogram2d(s1_dist.values(), s2_dist.values(), bins=10)
print "mutual information", mutual_information(hist_2d)