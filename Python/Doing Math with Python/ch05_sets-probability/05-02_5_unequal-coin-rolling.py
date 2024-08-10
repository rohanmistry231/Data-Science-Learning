'''
Purpose: demo a function to generate unequal probability
Author: Yasen Zhao
Date: 2024/02/24
'''
import random

def toss():
    # 0 -> Heads, 1 -> Tails
    if random.random() < 2/3:
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    for i in range(1,11):
        print(toss())