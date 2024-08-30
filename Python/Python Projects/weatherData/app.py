from flask import Flask, render_template,request
import requests
import configparser

app = Flask(__name__)

@app.route('/')
def weather_data():
    return render_template("index.html")

@app.route('/weatherdata', methods=['POST'])
def weather_results():
        city_name = request.form['cityname']
        api_key = get_api_key()
        data = get_weather_data(city_name, api_key)
        try:

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            main = data['weather'][0]['main']
            location = data['name']
            country = data['sys']['country']   
        except Exception:
            error = f"{city_name} is not a valid!"
            return error


        return render_template("results.html", 
            temp= temp,
            feels_like= feels_like,
            min_temp= min_temp,
            max_temp= max_temp,
            main= main,
            location= location,
            country= country
            )
        


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_data(city_name, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    res = requests.get(api_url)
    if res != "":
        return res.json()
    else:
        return city_name





if __name__=="__main__":
    app.run(debug=True)

