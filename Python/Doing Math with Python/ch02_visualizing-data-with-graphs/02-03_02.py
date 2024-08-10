# # Customizing Graphs - Adding a Title and Labels
# from pylab import plot, show, title, xlabel, ylabel, legend
# nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
# nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
# nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
# months = range(1, 13)
# plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
# title('Average monthly temperature in NYC')
# xlabel('Month')
# ylabel('Temperature')
# legend([2000, 2006, 2012])
# show()

# # Customizing Graphs - Customizing the Axes
# from pylab import plot, show, axis
# nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
# plot(nyc_temp, marker='o')
# # axis(ymin=30)
# show()