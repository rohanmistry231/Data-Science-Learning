# ******** PIE CHART ******** #

# Import libraries
from matplotlib import pyplot as plt
import numpy as np
 
 
# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
 
data = [23, 17, 35, 29, 12, 41]
 
# Creating plot
plt.pie(data, labels = cars,radius=1.2,autopct='%0.2f%%',shadow=True,explode=[0,0.2,0,0.1,0,0.1],startangle=45)
# autopct = to add % in your pie chart and 0.2 is used to print how many decimal values you want to print after point here 0.2 means 0.00% print :
# radius = radius is used to set radius of pie chart : 
# shadow = shodow gives a slide shadow in your pie chart :
# explode = explode is used to cut out a part and make that part little outside of your pie char :
# startangle = startangle is used to set angle of your pie chart :
# show plot
plt.show() 