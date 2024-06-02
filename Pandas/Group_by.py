import pandas as pd
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\Group_by.csv")
print(df)

# group by data by thier cities :

g = df.groupby('city')
print(g)
# it will create a object where you have keys and values here keys are 'new york,mumbai,paris' and values are other data :
# if you want to access all groups :

for city, city_df in g:
    print(city)
    print(city_df)

# if you want to access a particular group :

print("Only Mumbai")
p_group = g.get_group('mumbai')
print(p_group)

# find the maximum temperature in each of the city :

max_ = g.max()
print(max_) # in this what you're doing is :
# first you divide your data sets in group based on cities then,
# you're runnng analytics on each of this groups and then,
# you're combining the result into the single data frame :

# this process of dividing your data in groups and aplying some analytics to get aggregated result is called " split apply combined " :
# split : spliting data in groups :
# apply : apply operations on all groups (ex. max()) :
# combine : combine all result in single data frame :

# find avg of all cities :

avg_ = g.mean()
print(avg_)

# if you want to get all analytics in one shot then you can apply discribe() :

all_analytics = g.describe()
print(all_analytics)