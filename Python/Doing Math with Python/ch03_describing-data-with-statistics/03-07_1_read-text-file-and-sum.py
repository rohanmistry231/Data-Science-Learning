# Find the sum of numbers stored in a file
# Author: Yasen Zhao
# Date: 2024/02/18

def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print('Sum of the number in TXT fils is: {0}'.format(s))

if __name__ == '__main__':
    sum_data('mydata.txt')