'''
Purpose: prove the law of large numbers
Author: Yasen Zhao
Date: 2024/02/24
'''

import random
import matplotlib.pyplot as plt

def roll(num_trials):
    rolls=[]
    for t in range(num_trials):
        rolls.append(random.randint(1,6))
    return sum(rolls)/num_trials

if __name__ == '__main__':
    expected_value = 3.5
    print('Expected value: {0}'.format(expected_value))
    average_value = []
    trial_number = [100, 1000, 10000, 100000, 100000, 500000]
    for trial in trial_number:
        avg = roll(trial)
        average_value.append(avg)
        print('Trial: {0} with Trial average: {1}'.format(trial, avg))
    plt.plot(trial_number, average_value)
    plt.xlabel('trial')
    plt.ylabel('trial_average')
    plt.show()