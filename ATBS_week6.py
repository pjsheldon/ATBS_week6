'''--------By: PJ Sheldon---------
	--------Date: 8/15/20---------
	ATBS_week6.py debug coin toss
	SEC-290 Wilmington University'''

import random

guess = input('Guess the coin toss! Enter heads or tails: ') # first input question 
if guess != 'heads' and guess != 'tails':
    raise Exception('Guess must be heads or tails!') # validation 

GUESS_CONVERTER = {0: 'heads', 1: 'tails'}   # make the 0 ,  1 have values of heads and tails.
toss = GUESS_CONVERTER[random.randint(0, 1)] # 0 is tails, 1 is heads

if toss == guess:                         # first try
    print('You got it!')                  # if guessed on first try
    print()
    print('Thanks for playing')
    print()
    print('Game over')
else:                                     # did not guess on first try
    guess = input('Nope! Guess again!: ') # second try
    if toss == guess:                     # guessed right on the second try
        print('You got it!')              
        print()
        print('Thanks for playing')
        print()
        print('Game over')
    else:                                 # did not guess on second try either 
        print('Nope. You are really bad at this game.')
        print()
        print('Thanks for playing!!')
        print()
        print('Game over')
