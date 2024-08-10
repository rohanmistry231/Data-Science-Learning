'''
Purpose: Roll a die until totla score is n
Author: Yasen Zhao
Date: 2023/02/24
'''

import random
import matplotlib.pyplot as plt

def roll():
    return random.randint(1,6)

if __name__ == '__main__':
    target_score = int(input('Tell me the target score: '))
    score = 0
    num_rolls = 0
    every_score = []
    while score < target_score:
        die_roll = roll()
        num_rolls += 1
        print('Rolled in #{0} is {1}'.format(num_rolls,die_roll))
        score += die_roll
        every_score.append(die_roll)
    print('======Final Result======')
    print('Score of {0} reached in {1} rolls'.format(score, num_rolls))
    plt.plot(every_score) 
    plt.show()