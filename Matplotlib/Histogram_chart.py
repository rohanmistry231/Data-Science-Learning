# ********* HISTOGRAM CHART ********* #

import matplotlib.pyplot as plt
blood_sugar = [113,85,90,150,149,88,95,115,135,80,77,82,129]
plt.hist(blood_sugar,label='Suger level',bins=[80,100,125,150],rwidth=0.95,color='green')
plt.title('Blood-Sugar')
plt.legend()
# bins = bins means range between bars : ex : low level (80) , normal level (100) , medium level (125) , high level (150) :
# rwidth = relative width of bars
plt.show()
