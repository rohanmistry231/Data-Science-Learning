'''
Purpose: Calculating the mode when the list of numbers may have multiple modes
Author: Yasen Zhao
Date: 2024/02/15
'''

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    
    return modes

if __name__ == '__main__':
    scores = [4, 2, 2, 2, 1, 3, 4, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3]
    modes = calculate_mode(scores)
    print("The mode(s) of the list of {0}\nis: {1}".format(scores,modes))
    for mode in modes:
        print(mode)