'''
Purpose: Fining the Mode
Author: Yasen Zhao
Date: 2024/02/15
'''

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common()
    # return mode[0][0]
    return mode[0]

if __name__ == '__main__':
    scores = [4, 2, 1, 3, 4, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3]
    mode = calculate_mode(scores)
    print("The mode of the list of {0}\nis: {1}".format(scores,mode))