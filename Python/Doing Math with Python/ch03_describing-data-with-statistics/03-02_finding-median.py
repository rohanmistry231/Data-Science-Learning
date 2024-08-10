'''
Purpose: Find and calculate the Median
Author: Yasen Zhao
Date: 2024/02/15
'''

def calculate_median(numbers):
    n = len(numbers)
    numbers.sort()
    
    # find the median
    if n % 2 == 0:
        m1 = n / 2
        m2 = n / 2 + 1
        # convert to integer, match the position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (n + 1) /2
        # convert to integer, match the position
        m = int(1) - 1
        median = numbers[m]    

    return median

def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s/n
    return mean

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    median = calculate_median(donations)
    N = len(donations)
    print("Mean donation over the last {0} day is {1:.2f}".format(N, mean))
    print("Median donation over the last {0} day is {1}".format(N, median))