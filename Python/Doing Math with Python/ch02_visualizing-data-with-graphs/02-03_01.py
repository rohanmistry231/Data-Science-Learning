from pylab import plot, show, legend

# # Basic Plotting
# x_numbers = [1,2,3]
# y_numbers = [2,4,6]
# plot(x_numbers, y_numbers)
# show()

# # Basic Plotting with marker as 'o'
# x_numbers = [1,2,3]
# y_numbers = [2,4,6]
# plot(x_numbers, y_numbers, marker='D')
# show()

# # Basic Plotting with marker only as 'o', no line
# x_numbers = [1,2,3]
# y_numbers = [2,4,6]
# plot(x_numbers, y_numbers, 'o')
# show()

# # Graphing the Average Annual Temperature in New York City
# nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
# plot(nyc_temp, marker='o')
# show()

# # Graphing the Average Annual Temperature in New York City, with year in x-axis
# nyc_temp = [53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
# years = range(2000,2013)
# plot(years, nyc_temp, marker='o') # note: the maximum year is 2012
# show()

# # Comparing the Monthly Temperatur Trends of New York City
# nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
# nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
# nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
# months = range(1, 13)
# plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
# # [<matplotlib.lines.Line2D object at 0x000002081628EED0>, 
# #  <matplotlib.lines.Line2D object at 0x00000208185BAF90>, 
# #  <matplotlib.lines.Line2D object at 0x00000208185BB310>]
# show()

# # Comparing the Monthly Temperatur Trends of New York City, with Legend
# nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
# nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
# nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
# months = range(1, 13)
# plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
# # need import legend for showing Legend, legend() need after plot()
# legend(["Year 2000", "Year 2006", "Year 2012"])
# # legend([2000, 2006, 2012], loc="best") # use loc= to set location, by default is 'top right'
# show()