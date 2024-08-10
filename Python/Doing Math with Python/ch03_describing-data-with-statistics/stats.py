from collections import Counter

def mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s / n
    return mean

def median(numbers):
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

def mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]
    # return mode[0]

def variance_sd(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s / n
    diff = []
    for num in numbers:
        diff.append(num-mean)
    # Find the squared difference
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # print(squared_diff)
    sum_squared_diff = sum(squared_diff)
    print("Summary of Squared Difference is {0:.2f}".format(sum_squared_diff))
    variance = sum_squared_diff / len(numbers)
    sd = variance ** 0.5
    return variance, sd