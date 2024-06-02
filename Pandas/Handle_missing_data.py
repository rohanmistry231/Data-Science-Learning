import pandas as pd
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\Missing_weather_data.csv", parse_dates=["day"])
df.set_index('day',inplace=True)
print(df)
new_df = df.fillna(0)
print(new_df) # this .fillna function replace all NaN values with 0.0 :
# sometimes replacing 0 is not the best case :
# if you have to replace different values for different data set then we use dictionaries :
new_df = df.fillna({
    'temperature' : 0,
    'windspeed' : 0,
    'event' : 'No event'
})
print(new_df) # this will replace values by values that we have given in our dictinary :
# the other way of finding best case is  forward or backward values :
new_df = df.fillna(method='ffill') # ffill = forward fill is used to forward values : 
# means ex. 1st day temp  is 32 and 4th day temp is 0 so ffill forward 1st day value in 4th day :
print(new_df) 
# you can also use bfill = backward fill it will backward values :
# means ex. 5th day temp  is 28 and 4th day temp is 0 so bfill forward 1st day value in 4th day :
new_df = df.fillna(method='bfill')
print(new_df)

# if you want to forward or backward values horizontally so for that you can use axis='columns' :
# new_df = df.fillna(method='ffill',axis='columns')
# print(new_df) # it will forward values horizontally 

new_df = df.fillna(method='bfill',axis='columns')
print(new_df) # it will backward values horizontally 

# if you forward or backward value only one time then you can set limint :
# new_df = df.fillna(method='bfill',limit=1)
# print(new_df) # you can see that 4th month value is forward only ones 6th month remains NaN :
# index is day so you can't run this code in this program :
# for best case of replace values of front and rear values avg value for that you can use interpolate() function :
new_df = df.interpolate()
print(new_df) # interpolate() will find the best case to replace your date 
# ex. 1st day temp is 32 and 5th day temp is 28 and avg temp is 30 so interpolate() function replace midddle value with avg value 30 this is the best case to replace values :
print("***************************************")
new_df = df.interpolate(method="time")
print(new_df) # this is the best case ever when you replace values time by time it will replace 4th day value with avg of 1st and 5th day and then he set value as 4th day and replacde it :

# if you don't want to print any NaN values data set then you can use .dropna() func :
new_df = df.dropna()
print(new_df)
# if you don't want to print only those data who has all data as NaN then you can use 'how' :
new_df = df.dropna(how='all')
print(new_df) # this will print only those data who don't have any NaN values :

# if you want to print only those data who have only one or more than one NaN values then you can use thresold parameter thresh=NaN_counts :
new_df = df.dropna(thresh=1)
print(new_df)

# inserting the missing dates :
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)

# huuuuuuh last code is not working perferclty idn why if you find any way save it and send it to me :