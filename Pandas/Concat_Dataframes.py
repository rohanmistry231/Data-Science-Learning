# Concat Dataframes : merge/join two or more data frames :

import pandas as pd 

# creatng a data frames :

india_weather = pd.DataFrame({
    "City" : ["mumbai","delhi","banglore"],
    "Temperature" : [32,45,30],
    "Humidity" : [80,60,70]
})
print(india_weather)

us_weather = pd.DataFrame({
    "City" : ["new york","chicago","orlando"],
    "Temperature" : [21,12,35],
    "Humidity" : [60,45,75]
})
print(us_weather)

# concatination of data frames :

df = pd.concat([india_weather,us_weather])
print(df)

# if you want ignore index and print only one basic index then you can pass ignore index argument :

df = pd.concat([india_weather,us_weather],ignore_index=True)
print(df)

# if you want to retrive weather data from indian cities for this you can use keys :

df = pd.concat([india_weather,us_weather], keys=["india","us"])
print(df)

# if there is one unique coloumn in any data frame :

only_temp = pd.DataFrame(
    {
        "city" : ["surat","ahemdabad"],
        "temperature" : [32,42]
    }
)
print(only_temp)

only_windspeed = pd.DataFrame(
    {
        "city" : ["surat","ahemdabad"],
        "windspeed" : [7,12]
    }
)
print(only_windspeed)

# merging data frames :

df = pd.concat([only_temp,only_windspeed],sort=True)
print(df)

# if you want to add row instead of NaN values then you can use axis :

df = pd.concat([only_temp,only_windspeed],axis=1)
print(df)


# if there is missing data in any data frames :

# creating a data frame that have missing data :


miss_temp = pd.DataFrame(
    {
        "city" : ["surat","ahemdabad","Rajkot"],
        "temperature" : [32,42,40]
    }, index=[0,1,2]
)
print(miss_temp)
miss_windspeed = pd.DataFrame(
    {
        "city" : ["ahemdabad","surat"],
        "windspeed" : [7,12]
    },index=[1,0]
)
print(miss_windspeed)

# in second data frame Rajkot is missing and order of city is different to manage this data you can use index :

df = pd.concat([miss_temp,miss_windspeed],axis=1)
print(df)

# you can also append series in concatination :

# creating a series :
series_ = pd.Series(["Humid","dry","Rain"],name="event")
print(series_)

# appending series into data frames :

df = pd.concat([miss_temp,series_],axis=1)
print(df)

