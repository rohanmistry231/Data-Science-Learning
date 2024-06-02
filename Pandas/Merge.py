import pandas as pd

# creating some data frames :

df1 = pd.DataFrame(
    {
        "city" : ["surat","ahemdabad","Rajkot"],
        "temperature" : [32,42,40]
    }
)
print(df1)

df2 = pd.DataFrame(
    {
        "city" : ["surat","ahemdabad","Junagadh"],
        "windspeed" : [7,12,10],
    }
)
print(df2)

# mergig two data frames :

df = pd.merge(df1,df2,on="city")
print(df) # it will perform join operation of Sql :
# if you want to perform Inner/Outer/Left/right join then you can use "how" :

# outer join :
df = pd.merge(df1,df2,on="city",how="outer") # how = "inner" / "outer" / "left" / "right" :
print(df)
# inner jon :
df = pd.merge(df1,df2,on="city",how="inner") 
print(df)
# left join :
df = pd.merge(df1,df2,on="city",how="left") 
print(df)
# right join :
df = pd.merge(df1,df2,on="city",how="right") 
print(df)

# if you want to know which data is comming from which data set then you can use indicator argument :

df = pd.merge(df1,df2,on="city",how="outer",indicator=True) 
print(df)
