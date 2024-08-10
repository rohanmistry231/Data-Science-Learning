'''
Purpose: Finding the Percentile Score
Author: Yasen Zhao
Date: 2024/02/18
'''

from read_file import read_data_as_float

def find_percentile_score(data, percentile):
    
    n = len(data)
    data.sort()
    print(data)
    
    if percentile == 0:
        return data[0]
    
    if percentile == 100:
        return data[-1]
    
    i = n * percentile / 100 + 0.5
    print(i)
    
    if i.is_integer():
        real_index = int(i-1)
        return data(real_index)
    else:
        k = int(i)
        f = i - k
        real_index_1 = k - 1
        real_index_2 = k
        return (1-f)*data[real_index_1]+f*data[real_index_2]

if __name__ == '__main__':
    data = read_data_as_float('mydata1.txt')
    print(data)
    percentile = float(input("Please enter the percentile score you want to calculate (0~100): "))
    if percentile < 0 or percentile > 100:
        print("The Percentile should between 0 and 100!")
    else:
        percentile_score = find_percentile_score(data, percentile)
    print('The score at {0} percentile is: {1}'.format(percentile, percentile_score))
    