import requests

def current_weather():
    # will need to sign up and get your own API key from https://openweathermap.org
    url = "http://api.openweathermap.org/data/2.5/weather?q=san+diego%2Cca&units=imperial&appid=ENTER__APP_ID"
    r = requests.get(url)

    weather_json = r.json()
    print(weather_json)

    min = weather_json['main']['temp_min']
    max = weather_json['main']['temp_max']

    print("The circus' forecast is", min , "as the low and", max, "as the high")
