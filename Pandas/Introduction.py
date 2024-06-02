# ********** PANDAS LIBRARY ********** #

# how to import/read csv data set through dataFrames in pandas library :: 
import pandas as pd 
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\weather_data.csv")
# Data Munging or Data Wrangling means cleaning our data set : 
# if there is blank/NaN values in our data sets then we have to fill that data into 0 values otherwise our operations on data sets can't give exact value of operations :
# for making Nan into 0's we use "fillna" method and we have to add inplace=True for get that method property :
df.fillna(0,inplace=True)
# now we get the exact and accurate values :
print(df)
# finding max temperature :
max_temp = df["Temp"].max()
print(max_temp)
# finding which is rainy day :
rainy_day = df["Date"][df["RainToday"]=="Yes"]
print(rainy_day)
# finding average speed of windspeed :
avg_windspeed = df["WindSpeed"].mean()
print(avg_windspeed)