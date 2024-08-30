from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker


class Geopoint(Marker):

    def __init__(self, latitude, longitude ):
        super().__init__(location = [latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude

    def cloest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey = '26631f0f41b95fb9f5ac0df9a8f43c92', lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()

    @classmethod
    def random(cls):
        return cls(latitude= uniform(-90, 90)  , longitude = uniform(-180, 180))


class Antipode(Geopoint):

    def __init__(self, latitude, longitude, popup=None):

        self.latitude = latitude * -1

        if longitude <= 0:
            self.longitude = longitude + 180
        else:
            self.longitude = longitude - 180

        super().__init__(self.latitude, self.longitude)




tokyo = Geopoint(25.44, 78.56)
print(tokyo.cloest_parallel())
print(tokyo.get_time())
print(tokyo.get_weather())
print(tokyo.random())