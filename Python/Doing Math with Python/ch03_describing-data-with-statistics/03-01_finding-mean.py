'''
Purpose: Calculating the Mean
Author: Yasen Zhao
Date: 2024/02/15
'''

def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s/n
    return mean

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 900]
    mean = calculate_mean(donations)
    N = len(donations)
    print("Mean donation over the last {0} day is {1:.2f}".format(N, mean))