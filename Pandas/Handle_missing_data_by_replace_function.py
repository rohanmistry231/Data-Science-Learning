import pandas as pd
import numpy as np 
df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\Missing_data_replace_function.csv")
print(df)

# if you want to replace all -99999 value with NaN :
# new_df = df.replace(-99999,np.NaN)
# print(new_df)

# for more values if you want to replace then you have to use dictionaries :
new_df = df.replace({
    'temperature' : -99999,
    'windspeed' : [-99999,-88888],
    'event' : 'No event',
},np.NaN)
print(new_df)

new_df = df.replace({
    'temperature' : '[A-Za-z]',
    'windspeed' : '[A-Za-z]',
},'',regex=True)
print(new_df) # this will replace all a-z characters with ''(blank space) from temperature and windspeed columns :

# how can you replace list of values with another list of values :

# creating a database :
df = pd.DataFrame({
    'score' : ['exceptional','average','good','poor','average','exceptional'],
    'student' : ['rob','maya','parthiv','tom','julian','erica']
})
print(df)

# replace all 'exceptional','average','good','poor','average','exceptional' with [1,2,3,4] :

new_df = df.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(new_df)
