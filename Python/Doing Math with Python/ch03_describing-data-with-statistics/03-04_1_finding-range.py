'''
Purpose: Find the Range of a list of number
Author: Yasen Zhao
Date: 2024/02/15
'''

def find_range(numbers):
    
    lowest = min(numbers)
    highest = max(numbers)
    
    # find the range
    range = highest - lowest
    
    return lowest, highest, range

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, range = find_range(donations)
    print('Lowest: {0}, Highest: {1} and Range: {2}'.format(lowest, highest, range))