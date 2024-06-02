# ********* MATPLOT LIBRARY ********* #

# ********* INTRODUCTION ********* #

# plotting a weather chart ::

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Weather chart')
plt.plot( x,y, color='green' , linewidth=5 , linestyle='dotted' , marker='^' , markersize=10 , alpha=0.5)
# instead of color and linestyple you directly type this command : 'g--' it will understand like green color and -- linestyle :
# some basic properties of ploting a graph ::
# color : change color :
# lindwidth : change the widht of line :
# linestyle : change the style of line :
# marker : change the pointer style
# markersize : change the pointer size
# aplha : change the opacity of graph 
plt.show()