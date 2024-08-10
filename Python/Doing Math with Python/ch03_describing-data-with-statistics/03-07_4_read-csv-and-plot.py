'''
Purpose: read from csv file and do plotting
Author: Yasen Zhao
Date: 2024/02/18
'''

import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
        return numbers, squared

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel("Number")
    plt.ylabel("Square")
    plt.show()

if __name__ == '__main__':
    numbers, squared = read_csv('numbers.csv')
    print(numbers)
    print(squared)
    scatter_plot(numbers,squared)