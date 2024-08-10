'''
Purpose: demo the shuffle of one number list from 1 to 52
Author: Yasen Zhao
Date: 2024/02/25
'''

import random

def shuffle_and_print(list):
    random.shuffle(list)
    print(list)
    
if __name__ == '__main__':
    num_list = []
    num_list_to_suffle = []
    for i in range(1,53):
        num_list.append(i)
        num_list_to_suffle.append(i)
    print(num_list)
    shuffle_and_print(num_list_to_suffle)
    print(num_list)