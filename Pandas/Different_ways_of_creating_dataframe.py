# read data from csv file :
print("Read Data from csv file :")
import pandas as pd 
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\Weather.csv")
print(df)
# read data from excel file :
print("")
print("Read Data from excel file")
df = pd.read_excel("C:\\Users\\Rohan S Mistry\\Downloads\\Weather_exel.xlsx","Weather")
print(df) 
# create data frame using python dictionary :
print("")
print("Creating Data with Dictionray :")
weather_data = {
    'day' : ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature' : [32,35,28,24,32,32],
    'windspeed' : [6,7,2,7,4,2],
    'event' : ['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(weather_data)
print(df)

# create data frame using python tupple :
print("")
print("Creating data using tupple :")
weather_data_tupple = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow'),
    ('1/4/2017',24,7,'Snow'),
    ('1/5/2017',32,4,'Rain'),
    ('1/6/2017',32,2,'Sunny')
]
data_tupple = pd.DataFrame(weather_data_tupple,columns=['day','temperature','windspeed','event'])
print(data_tupple)

# create data frame using list of dictionaries :
print("")
print("Creating data using list of dictionaries :")
weather_data_list_dic = [
    {'day':'1/1/2017','temperature':32,'windspeed':6,'event':'Rain'},
    {'day':'1/2/2017','temperature':35,'windspeed':7,'event':'Sunny'},
    {'day':'1/3/2017','temperature':28,'windspeed':2,'event':'Snow'},
    {'day':'1/4/2017','temperature':24,'windspeed':7,'event':'Snow'},
    {'day':'1/5/2017','temperature':32,'windspeed':4,'event':'Rain'},
    {'day':'1/6/2017','temperature':32,'windspeed':2,'event':'Sunny'}
]
data_list_dic = pd.DataFrame(weather_data_list_dic)
print(data_list_dic)