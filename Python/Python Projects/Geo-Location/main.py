from folium import Map, Marker, Popup
from geo import Geopoint, Antipode

locations = [[25.44, 78.56]]



#folium map instance
mymap = Map(location = [25.44, 78.56])

for lat, lon in locations:
    geopoint = Antipode(latitude=lat, longitude=lon)
    forcast = geopoint.get_weather()

    popup_content = f"""
    {forcast[0][0][-8:-6]}h: {forcast[0][1]}°F <img src=" http://openweathermap.org/img/wn/{forcast[0][-1]}@2x.png" width=55 >
    <hr style="margin:2px;">
    {forcast[1][0][-8:-6]}h: {forcast[1][1]}°F <img src=" http://openweathermap.org/img/wn/{forcast[0][-1]}@2x.png" width=55 >
    <hr style="margin:2px;">
    {forcast[2][0][-8:-6]}h: {forcast[2][1]}°F <img src=" http://openweathermap.org/img/wn/{forcast[0][-1]}@2x.png" width=55 >
    <hr style="margin:2px;">
    {forcast[3][0][-8:-6]}h: {forcast[3][1]}°F <img src=" http://openweathermap.org/img/wn/{forcast[0][-1]}@2x.png" width=55 >
    <hr style="margin:2px;">
    """

    popup = Popup(popup_content, max_width=450)
    # popup =popup(str(geopoint.get_weather()))
    popup.add_to(geopoint)
    geopoint.add_to(mymap)


#saving map instance into a HTML file
mymap.save('map.html')