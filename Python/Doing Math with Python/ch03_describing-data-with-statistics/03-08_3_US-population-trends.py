'''
Purpose: US Population Trends analysis from CSV
Author: Yasen Zhao
Date: 2024/02/18
'''

import matplotlib.pyplot as plt
import csv
from stats import mean, median, variance_sd

def read_csv(filename):
    years = []
    population = []
    
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            years.append(row[0].split('/')[0]) # split from yyyy/mm/dd then choose yyyy only via [0]
            population.append(float(row[1]))
    
    return years, population

def plot_population(years, population):
    plt.figure(1)
    xaxis_positions = range(0, len(years))
    plt.plot(population, 'r-')
    plt.title('Total Population in US')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(xaxis_positions, years, rotation=45)

def calculate_stats(population):
    growth = []
    for i in range(0, len(population)-1):
        growth.append(population[i+1] - population[i])
    print('Mean growth: {0:.5f}'.format(mean(growth)))
    print('Median growth: {0:.5f}'.format(median(growth)))
    print('Variance/SD growth: {0:.5f}, {1:.5f}'.format(*variance_sd(growth)))
    return growth

def plot_population_diff(growth, years):
    xaxis_positions = range(0, len(years)-1)
    xaxis_labels = ['{0}-{1}'.format(years[i], years[i+1]) for i in range(len(years)-1)]
    plt.figure(2)
    plt.plot(growth, 'r-')
    plt.title('Population Growth in consecutive years')
    plt.ylabel('Population Growth')
    plt.xticks(xaxis_positions, xaxis_labels, rotation=45)

if __name__ == '__main__':
    years, population = read_csv('03-08_3_US-Population.csv')
    # print(years, population)
    plot_population(years, population)
    growth = calculate_stats(population)
    plot_population_diff(growth, years)
    plt.show()