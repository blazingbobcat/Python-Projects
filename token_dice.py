# Data program dice-token game
# Josh Klipstein

# April 23, 2021

from random import *
from math import *

# Game classes go here
class Die(object):
    def __init__(self, num):
        self.number = num

    def __del__(self):
        print("Die deleted")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, num):
        self.__number = num

# Introduce user to program

doc = '''
    Welcome!  This is a simulation of a token and dice game.  It will play
    however many games the user enters and output won and lost games.  The
    user can infer from this data what the odds are for winning the game in
    real life.
'''
print(doc)

# Prompt for number of games and store in variable
num = input("Please enter number of games: ")

# If an invalid value (e.g. negative), reprompt for number
while (num.isdigit() == False or int(num) < 0):
    num = input("Invalid input.  Please enter number of games: ")

# Create appropraite objects and variables for game
dice = []
for i in range(2):
    dice.append(Die)

games = int(num)

wonGames = 0
lostGames = 0

# Main loop
for g in range(games):

    # New tokens list
    tokens = [i for i in range(1,10)]

    # Game object loop
    done = False
    while not done:
        diceSum = 0
        indexOne = 0
        indexTwo = 0
        tokenSum = 0
        
        # Roll 2 virtual dice objects
        for d in dice:
            d.number = randint(1,6)
            diceSum += d.number

        #print("Dice Sum: {0}".format(diceSum)) # DEBUG

        # CHeck if relevant tokens in game objecct equal sum of dice
        for i in tokens:
            for j in tokens[i:]:
                if diceSum == i + j:
                    indexOne = i
                    indexTwo = j
                    tokenSum = indexOne + indexTwo

        #print("Token Sum: {0}".format(tokenSum)) # DEBUG

        if diceSum == tokenSum:
            tokens.remove(indexOne)
            tokens.remove(indexTwo)
        else:
            # If games left is zero, exit loop and read number of won and lost games
            #print(tokens) # DEBUG
            if tokens == []:
                wonGames += 1
            else:
                lostGames += 1
            done = True
                
# Output number of won and lost games
for die in dice:
    del die
print("Number of won games: {0}\nNumber of lost games: {1}".format(wonGames,
                                                                   lostGames))

# End program
