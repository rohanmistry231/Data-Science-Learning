# ********* HISTOGRAM CHART ********* #

import matplotlib.pyplot as plt
blood_sugar_man = [113,85,90,150,149,88,95,115,135,80,77,82,129]
blood_sugar_women = [67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.hist([blood_sugar_man,blood_sugar_women],label=['man','women'], bins=[80,100,125,150], rwidth=0.95, color=['green','orange'])
plt.title('Blood sugar analysis')
plt.xlabel('Sugar range')
plt.ylabel('Total no of patients')
plt.legend()
# bins = bins means range between bars : ex : low level (80) , normal level (100) , medium level (125) , high level (150) :
# rwidth = relative width of bars
plt.show()
