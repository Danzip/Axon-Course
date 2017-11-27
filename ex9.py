from random import *

guesses=0
while True:
    r = randint(1, 9)
    while True:
        guess=int(raw_input("guess a number between 1-9"))
        guesses+=1
        if guess>r:
            print "you guessed to high try again"
        elif guess<r:
            print "to low"
        else:
            print "You guessed right!"
            break
    kg=raw_input("would you like to continue playing y/n?")
    if kg=='n':
        print "You've guessed %s Times" %(guesses)
        break