# plotting more than one chart in one chart ::

import matplotlib.pyplot as plt 
days = [1,2,3,4,5,6,7]
max_temp = [50,51,52,48,47,49,46]
min_temp = [43,42,40,44,33,35,37]
avg_temp = [45,48,48,46,40,42,41]
plt.xlabel=('Days')
plt.ylabel=('Temperature')
plt.title=('Weather chart')
plt.plot(days,max_temp, label='Max')
plt.plot(days,min_temp, label='Min')
plt.plot(days,avg_temp, label='avg')
plt.legend(loc='lower left', shadow=True , fontsize='large') 
# to enable label properties of plt.plot you have to add plt.legend() method :
# loc is used to locate your legend if you write 'best' in loc it will place legend to best free space of your graph :
# shodow property True means it will create a shodow of legend :
# fontsize is used to change the size of font of legend :
plt.grid() # it will create a grid in your graph for better understanding :
plt.show() # it is mendatory to show your graph :