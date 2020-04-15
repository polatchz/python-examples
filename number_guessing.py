#import packages
from random import randint

print("Welcome number guessing game")
round = int(input("How many numbers would you like to guess?"))
live = 3


for i in range(round):
    value = randint(0,100)
    predict = int(input("please enter your guess"))
    
    if predict==value:
        print("Correct answer")
    else:
        print("Incorrect answer")
        live=live-1
        print("Left live",live)
        if live==0:
            print("Lost this game")
            break
