import pandas as pd
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\Weather.csv")
print(df)
print("")
# Creating dataset using dictionaries :
print("Creating DataSet Using Dictionaries : ") 
print("")
weather_data = {
    'day' : ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature' : [32,35,28,24,32,32],
    'windspeed' : [6,7,2,7,4,2],
    'event' : ['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(weather_data)
print(df)
# shape of data set (Dimension of data set) :
shape = df.shape
print(shape) # it will print 6,4 means 6 rows and 4 columns :
# if you have large number of data set but you want to print first 5/10(some) data so for this we use head() command :
head = df.head(2)
print(head) 
# if you write .head() it will print first some values 
# but if you wrtie .head(2) it will give you first 2 rows :

# if you print last some data instead of printing large size data for this we use tail() command :
tail = df.tail(2)
print(tail)
# if you write .tail() it will print last some values 
# but if you wrtie .tail(2) it will give you last 2 rows :

# Indexing & Slicing of data set :

two_five = df[2:5]
print(two_five) # it will print 2,3,4 rows :
# there are many other values :
# print everything : df[:] etc...

# print columns :
col = df.columns
print(col)
# print individual column :
day = df.day
print(day)
# print more than one column :
event_day = df[['event','day']]
print(event_day)

# if you want to print all statistics of your data then discribe function used :
statistics = df.describe()
print(statistics)

# if you want some condtional datasets only then we use conditions :
con = df[df.temperature>=32]
print(con) # it will print only those data whome teperature is greater than 32 :

# printing only those values that you want like :
only = df[['day','temperature']][df.temperature==df['temperature'].max()] 
# df['temperature'].max() can also be written as df.temperature.max() but sometimes if you have some those data sets 
# who contains some spaces then we have to use this type of syntax like value is 'wind speed' then you cant use df.wind speed.max() it will give you error. 
# thats why preventing this type of errors we use df['wind speed].max()  this type of syntax :
print(only)

# print index :
index = df.index
print(index)

# if you want to set particular column as your index :
day_index = df.set_index('day',inplace=True)
print(day_index)

# if you want to print particular day data :
day_one = df.loc['1/1/2017']
print(day_one)

# if you want to reset your index with original one :
reset_index = df.reset_index(inplace=True)
print(df)