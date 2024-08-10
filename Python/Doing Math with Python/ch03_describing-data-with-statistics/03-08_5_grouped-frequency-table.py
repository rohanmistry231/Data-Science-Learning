'''
Purpose: Create one Grouped Frequency Table
Author: Yasen Zhao
Date: 2024/02/18
'''

from read_file import read_data_as_float

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    
    # Width of each class
    width = (high - low) / n
    classes = []
    a = low
    b = low + width
    while a < (high - width):
        classes.append((a,b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    
    return classes

def classify(numbers, classes):
    count = [0]*len(classes)
    for n in numbers:
        for index, c in enumerate(classes):
            if n >= c[0] and n < c[1]:
                count[index] = count[index] + 1
                break
    return count

if __name__ == '__main__':
    num_classes = int(input('Enter the number of classes: '))
    data = read_data_as_float('mydata2.txt')
    print(data, num_classes)
    classes = create_classes(data,num_classes)
    print(classes)
    count = classify(data, classes)
    print(count)
    print('Classes\t\tCount')
    for c, cnt in zip(classes, count):
        print('{0:.2f}-{1:.2f}\t{2}'.format(c[0], c[1], cnt))