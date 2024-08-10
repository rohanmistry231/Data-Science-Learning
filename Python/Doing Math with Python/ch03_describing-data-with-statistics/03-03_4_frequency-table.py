'''
Purpose: Frequency table for a list of number
Author: Yasen Zhao
Date: 2024/02/15
'''

from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    print('-'*30)
    print('Number\t|\tFrequency')
    print('-'*30)
    for number in table.most_common():
        print('{0}\t|\t{1}'.format(number[0], number[1]))
    print('-'*30)

if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,1,10]
    frequency_table(scores)