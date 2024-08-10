# Calculating the mean of numbers stored in a file
# Author: Yasen Zhao
# Date: 2024/02/18

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

def calculate_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s/n
    return mean

if __name__ == '__main__':
    data = read_data('mydata.txt')
    print(data)
    mean = calculate_mean(data)
    print('Mean: {0:.2f}'.format(mean))