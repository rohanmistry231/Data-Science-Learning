'''
Purpose: Relation between Fibonacci Sequence and Golden Ratio
Author: Yasen Zhao
Date: 2024/02/14
'''

import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series

# def draw_graph(x, y):
#     plt.plot(x, y, marker='o')
#     plt.title("Fibonacci Sequence in Line Chart")
#     plt.show()

def plot_ratio(series):
    ratios = []
    for i in range(len(series)-1):
        ratios.append(series[i+1]/series[i])
    plt.plot(ratios)
    plt.title("Ratio between Fibonacci Number and Golden Ratio")
    plt.xlabel('No.')
    plt.ylabel("Ratio")
    plt.show()

if __name__ == '__main__':
    n = int(input("Fibonacci Sequence till which number? "))
    series = fibo(n)
    plot_ratio(series)