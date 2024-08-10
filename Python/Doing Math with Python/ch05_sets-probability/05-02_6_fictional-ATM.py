'''
Purpose: Simulate a fictional ATM that dispeneses dollor bills
    of various denominations with varying probability
Author: Yasen Zhao
Date: 2024/02/24
'''

import random

def get_index(probability):
    c_probability = 0
    sum_probability = []
    
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    
    r = random.random()
    print(r)
    
    for index, sp in enumerate(sum_probability):
        if r <= sp:
            return index
    return len(probability) - 1

if __name__ == '__main__':
    dollor_bills = [5, 10, 20, 50]
    probability = [1/12, 1/12, 1/3, 1/2]
    bill_index = get_index(probability)
    print(dollor_bills[bill_index])