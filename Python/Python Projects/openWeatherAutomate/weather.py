import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date


api_key= "**********************"
india_list = ['Jhansi','Jaipur', 'Indore', 'Pune', 'Bengaluru']
usa_list = ['New York','Chicago', 'San Francisco', 'Los Angeles', 'San Diego']

country_list = [india_list, usa_list]
positions = [300, 430, 560, 690, 820]

for country in country_list:
    image = Image.open('post.png')
    draw = ImageDraw.Draw(image)

    title_font = ImageFont.truetype('roboto.ttf', size=50)
    title = "Current Weather Forecast"
    color = "rgb(255,255,255)"
    (x, y) = (279,45)
    draw.text((x, y), title, color, font=title_font)

    title_font = ImageFont.truetype('roboto.ttf', size=40)
    today = date.today()
    title =  today.strftime("%A - %B %d, %Y")
    color = "rgb(255,255,255)"
    (x, y) = (315,135)
    draw.text((x, y), title, color, font=title_font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=********&units=metric".format(city)
        response = requests.get(url)
        data = json.loads(response.text)

        title_font = ImageFont.truetype('roboto.ttf', size=40)
        color = "rgb(0,0,0)"
        (x, y) = (135, positions[index])
        draw.text((x, y), city, color, font=title_font)

        title_font = ImageFont.truetype('roboto.ttf', size=40)
        title = str(data['main']['temp']) + '\u00b0'
        color = "rgb(255,255,255)"
        (x, y) = (600,positions[index])
        draw.text((x, y), title, color, font=title_font)

        title_font = ImageFont.truetype('roboto.ttf', size=40)
        title =  str(data['main']['humidity']) + '%'
        color = "rgb(255,255,255)"
        (x, y) = (800, positions[index])
        draw.text((x, y), title, color, font=title_font)

        index += 1


    image.save(f"{country[0]}.png")
    image = image.convert('RGB')
    image.save(f"{country[0]}.pdf")
