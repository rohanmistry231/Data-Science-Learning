# Pandas

This section covers Pandas, a powerful data manipulation and analysis library for Python.

## Topics Covered
- Introduction to Pandas
- Series and DataFrame
- Data indexing and selection
- Data cleaning and preprocessing
- Data aggregation and grouping
- Merging and joining datasets

## Resources
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Pandas Tutorial](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

## Code Examples

```python
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# DataFrame operations
print(df.describe())
print(df[df['Age'] > 30])