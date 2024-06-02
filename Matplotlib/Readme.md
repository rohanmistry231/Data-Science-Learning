# Matplotlib

This section covers Matplotlib, a plotting library for creating static, animated, and interactive visualizations in Python.

## Topics Covered
- Introduction to Matplotlib
- Creating basic plots (line, scatter, bar)
- Customizing plots (titles, labels, legends)
- Subplots and multiple plots
- Saving and displaying plots

## Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

## Code Examples

```python
import matplotlib.pyplot as plt

# Creating a simple plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Simple Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()