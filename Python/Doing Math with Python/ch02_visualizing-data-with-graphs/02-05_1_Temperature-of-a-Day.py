'''
Purpose: city temperature forecast of a day
Author: Yasen Zhao
Date: 2024/02/14
'''

import matplotlib.pyplot as plt

def plot_forecast():
    time_of_day_nyc = ['11 AM', '2 PM', '5 PM', '8 PM', '11 PM', '2 AM', '5 AM', '8 AM']
    nyc_temp = [-2, 1, 2, -1, -2, -3, -3, -4]
    brisbane_temp = [25, 23, 24, 28, 29, 28,26, 24]
    toronto_temp = [-4, -1, 1, -2, -5, -5, -4, -2]
    amsterdam_temp = [12, 11, 11, 11, 11, 11, 12, 14]
    
    plt.plot(
        time_of_day_nyc, nyc_temp,
        time_of_day_nyc, brisbane_temp,
        time_of_day_nyc, toronto_temp,
        time_of_day_nyc, amsterdam_temp,
        marker='*'
    )
    plt.legend(["New York City", "Brisbane", "Toronto", "Amsterdam"], loc='best')
    plt.title("Cities Temperature Forcast of the day - 2024/02/14, using NYC Time")
    plt.xlabel("hour")
    plt.ylabel("Temperature")
    plt.grid('on')
    plt.ylim((-10,50))
    plt.show()

if __name__ == '__main__':
    plot_forecast()