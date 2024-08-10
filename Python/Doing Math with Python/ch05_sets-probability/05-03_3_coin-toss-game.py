'''
Purpose: Coin toss game, which will be over when the player's balance reaches $0
Author: Yasen Zhao
Date: 2024/02/24
'''

import random

def play(start_amount):
    head_amount = 1     # head refers to toss=0
    tail_amount = -1.5  # tail refers to toss=1
    
    outstanding_amount = start_amount
    tosses = 0
    
    while outstanding_amount > 0:
        toss = random.randint(0,1)
        tosses = tosses + 1
        if toss == 0:
            outstanding_amount += head_amount
            print('Heads! Outstanding amount: {0:.1f}'.format(outstanding_amount))
        else:
            outstanding_amount += tail_amount
            print('Tails! Outstanding amount: {0:.1f}'.format(outstanding_amount))
    
    print('Game Over! ;-( Outstanding amount: {0:.1f}. Coin tosses: {1}'.format(outstanding_amount, tosses))

if __name__ == '__main__':
    start_amount = float(input('Please enter the staring amount: '))
    play(start_amount)