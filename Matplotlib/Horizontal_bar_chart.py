# plotting a bar chart ::

import matplotlib.pyplot as plt
import numpy as np
company = ['Google','Amazon','Microsoft','Facebook']
revenue = [90,136,89,27]
profit = [40,2,34,12]
plt.title('Us Tech Stocks')
# bar char dosen't honours(accept) the string values so,..
# we will create a ypos(yposition) array :
xpos = np.arange(len(company)) 
plt.yticks(xpos,company)
# here direct values of company name is print in graph...
# but incase values(name) of company dosent print and print range between 0 to 4 than you have to use xticks function :
# xticks function synatx : plt.xticks(ypos,company) : here 0 will be replace by Google and so on...! :
plt.barh(xpos-0.2, revenue , label='Revenue') # barh used for plotting horizontal bar chart :
plt.barh(xpos+0.2, profit, label='profit') 
plt.legend()
plt.show()