#functions with return and without params

from random import randint
import os

def rollDice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1, die2

#Main
os.system('clear')

dice = rollDice()
print (f"Dice:{dice}")
if dice[0] == 6 and dice[1] == 6:
    print("You win!!!")

else:
    print("Try again!")