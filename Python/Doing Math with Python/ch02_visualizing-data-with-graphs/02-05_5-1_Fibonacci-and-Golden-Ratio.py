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

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.title("Fibonacci Sequence in Line Chart")
    plt.show()
    

if __name__ == '__main__':
    # print(fibo(10))
    n = int(input("Fibonacci Sequence till which number? "))
    x = []
    for i in range(n+2):
        x.append(i)
    y = fibo(n)
    draw_graph(x, y)
    