# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:01:02 2019

@author: jdimond
"""

from random import randint
randnum = randint(1,100)
#print(randnum)
guessed_num = []
#print(len(guessed_num))
def game():
    guess = int(input("guess the number: "))
    if len(guessed_num) != 0:
        last_guess = guessed_num[len(guessed_num)-1]
    if guess == randnum:
        print("Congratulations! You win the game, it took " + str(len(guessed_num)+1) +" guesses")
        return game
    elif len(guessed_num) == 0:
            if guess < 1 or guess > 100:
                print("OUT OF BOUNDS")
            elif guess in range(randnum -10,randnum +11):
                print("WARM!")
            else:
                print('COLD!')
            guessed_num.append(guess)
    else:
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS")
        elif abs(randnum - guess) < abs(randnum - last_guess):
            print("WARMER!")
        else:
            print('COLDER!')
        guessed_num.append(guess)
#        print(guessed_num)
#        print(last_guess)
    game()
    
game()