from math import *
string=raw_input("enter a string")
pali_bool=True
for i in range(int(ceil(len(string)/2))):
    print i
    if string[i]!=string[len(string)-i-1]:
        print("not a palindrome")
        pali_bool=False

if pali_bool:
    print("string is a palindrome")