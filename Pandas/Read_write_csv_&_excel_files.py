import pandas as pd 

def converter_event_cell(cell): # if you want to print some default value you have to use converter :
    if cell=='n.a.':
        return 'Sunny'
    return cell

df = pd.read_csv("C:\\Users\\Rohan S Mistry\\Downloads\\weather_data_set.csv",skiprows=1,na_values={
    'temperature' : ["not_available","n.a."],
    'windspeed' : ["not_available","n.a.",-4] # this is not working in our program but it is right syntax to change values with na_values :
},converters = {
    'event' : converter_event_cell # converter always use dictionaries :
}) 
# skiprows or header = 1
# when there is a extra header in your file like in this file "Weather data" and if you want to skip that row then skiprows or header function used :
# if there is n.a./not_available values in your data set and you want to set that as NaN then na_values is used :
# now windspeed would never be -3. so if you want to change that value with NaN then :
print(df)