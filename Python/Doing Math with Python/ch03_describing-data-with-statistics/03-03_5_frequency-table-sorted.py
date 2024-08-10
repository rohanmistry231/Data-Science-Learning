'''
Purpose: Frequency table for a list of number, enhanced to display the table sorted by the numbers
Author: Yasen Zhao
Date: 2024/02/15
'''

from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    print(numbers_freq)
    numbers_freq.sort()
    print(numbers_freq)
    print('-'*30)
    print('Number\t|\tFrequency')
    print('-'*30)
    for number in numbers_freq:
        print('{0}\t|\t{1}'.format(number[0], number[1]))
    print('-'*30)

if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,1,10]
    frequency_table(scores)