import os
import json
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')  # API Key
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('weather.html')
    location = request.form.get('name')
    print(location)
    url = "http://api.weatherapi.com/v1/current.json?key={0}&q={1}".format(api_key, location)
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raises an HTTPError for bad responses
        data = res.json()
        obj1 = data["location"]
        obj2 = data["current"]
        location_name = obj1["name"]
        region_name = obj1["region"]
        country_name = obj1["country"]
        temperature_inCelsius = str(obj2["temp_c"]) + " °C"
        temperature_inFarenheit = str(obj2["temp_f"]) + " °F"
        humidity = str(obj2["humidity"]) + "%"
        wind_speed = str(obj2["wind_kph"]) + " Kmph"
        wind_direction = str(obj2["wind_dir"])
        feels_like = str(obj2["feelslike_c"]) + " °C"
        text = obj2["condition"]["text"]
        icon = "https:" + obj2["condition"]["icon"]
        last_updated=obj2["last_updated"]
        Precipitation =obj2["precip_mm"]
        return render_template('weather.html', loc=location_name, reg=region_name, coun=country_name,
                               tc=temperature_inCelsius, tf=temperature_inFarenheit, cond=text,
                               winspd=wind_speed, windir=wind_direction,humi=humidity,precip_mm=Precipitation,felk=feels_like, img=icon,lup=last_updated)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return render_template('weather.html', error="Unable to fetch weather data. Please try again.")

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
