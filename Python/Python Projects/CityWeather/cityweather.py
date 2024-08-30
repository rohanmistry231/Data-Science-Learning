import requests, pprint

'''
For Weather Forecast:

Creates a Weather object getting an apikay as input
and either a city name ot langitude(lan) or longitude(lon)
Pacakage use example:
    # Create a weather object using a city name.
    # Response depend on the API key.
    # Get your own API key from Open Weather Map

    >>> cityweather = Weather(
    apikey = '**************', city='Pune')

    # Using latitude and longitude coordinates
    >>> cityweather = Weather(apikey = '**************', lon='78', lan='56')

    # Complete Weather data for next 12 hours, with every 3 hours period
    >>> cityweather.next12h()

    # Simplified data for the next 12 hours, for every 3 hours period
    >>> cityweather.next12h_simpliflied()

    # url to find sky condions icons:
    # change the 2x.png with other values(10d.png)
    >>>  http://openweathermap.org/img/wn/10d@2x.png

'''

class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):
            if city:
                url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
                res = requests.get(url)
                self.data = res.json()
            elif lat and lon:
                url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
                res = requests.get(url)
                self.data = res.json()
            else:
                raise TypeError("You need to provide either a city name ot Lat and Lon arguments")

            if self.data['cod'] != '200':
                raise ValueError(self.data['message'])


    def next_12h(self):
        #Weather forecast for 12 hours, with every next three hours.
        return self.data['list'][:4]

    def next_12h_simplified(self):
        '''
        Simplified data with date, time, temprature, and sky condition every 3 hours for the next 12 hours.
        '''
        weatherdata = []
        for i in self.data['list'][:4]:
            weatherdata.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description'], i['weather'][0]['icon']))
        return weatherdata



cityweather = Weather(
    apikey = '761dbb0f3e03407e21ef902de54f9b2c', city='Pune' )





"""
For Today's Weather Details:
Create a WeatherToday object getting an apikey and a city name as a input.

Package use example:

# Create a weathertoday object using a city name.
# Response entirly dependent on the API key.
# Get your own API key from Open Weather Map

    >>> cityweather = Weather(
    apikey = '**********', city='Pune')

    # Complete Weather data for today
    >>> cityweather.todayweatherdetails()

    # Simplified weather data for today with few  clear inormation like; Max & Min temp, wind, humidity
    >>> cityweather.todayweatherdetailsSimplified()

"""

class WeatherToday:

    def __init__(self, apikey, city):
        if city:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=761dbb0f3e03407e21ef902de54f9b2c&units=metric".format(city)
            res = requests.get(url)
            self.data = res.json()
        else:
            raise TypeError("You need to provide a city name arguments")

    def todayweatherdetails(self):
        #Today's Complete Weather Data!
        return self.data


    def todayweatherdetailsSimplified(self):
        #Today's weather data simplified with fewer details

        weatherdata = []
        weatherdata.append(f"City:{self.data['name']}, Max Temp: {self.data['main']['temp_max']}, Min Temp: {self.data['main']['temp_min']}, Humidity: {self.data['main']['humidity']}, Description: {self.data['weather'][0]['description']}, Wind Speed:{self.data['wind']['speed']}")
        return weatherdata


cityweather = WeatherToday(
    apikey = '761dbb0f3e03407e21ef902de54f9b2c', city='Jhansi' )




'''
To run the cityweather library in Python Shell

### Find help
>>> help(cityweather.Weather)
>>> help(cityweather.WeatherToday)

### use the cityweather library in shell command
>>> cityweather = Weather(
    apikey = '**************', city='Pune')

>>> cityweather.next12h_simpliflied()

'''