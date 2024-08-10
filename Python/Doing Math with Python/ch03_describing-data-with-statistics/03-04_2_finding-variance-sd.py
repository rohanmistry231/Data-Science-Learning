'''
Purpose: Find the variance and standard deviation (SD)
Author: Yasen Zhao
Date: 2024/02/15
'''

def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s / n
    print(mean)
    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    print(diff)
    return diff

def calculate_variance(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared difference
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    print(squared_diff)
    sum_squared_diff = sum(squared_diff)
    print("Summary of Squared Difference is {0:.2f}".format(sum_squared_diff))
    variance = sum_squared_diff / len(numbers)
    return variance

if __name__ == '__main__':
    # donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    donations = [500, 500, 503, 600]
    # calculate_mean(donations)
    # find_differences(donations)
    variance = calculate_variance(donations)
    print("The variance of the list of numbers is {0:.2f}".format(variance))
    std = variance ** 0.5
    print("The standard deviation of the list of numbers is {0:.2f}".format(std))