from math import *


def divisibles():
    divis=[]
    number=int(raw_input("enter a number bitch"))
    for x in range (2,number):
        if number%x==0:
            divis.append(x)
    return divis

