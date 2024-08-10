'''
Purpose: Statistics Calculator
Feature: 1) read from text file 2) use self definded library
Author: Yasen Zhao
Date: 2024/02/18
'''

from stats import mean, median, mode, variance_sd
from read_file import read_data_as_float

if __name__ == '__main__':
    data = read_data_as_float('mydata.txt')
    print(data)
    print("Mean is {0}".format(mean(data)))
    print("Median is {0}".format(median(data)))
    print("Mode is {0}".format(mode(data)))
    variance, sd = variance_sd(data)
    print("Variance is {0}, Sd is {1}".format(variance,sd))