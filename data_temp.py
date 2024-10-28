import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "cec1de6786fa2cdfdd123c10c3407749"
CITY = input("Enter city name: ")

url = BASE_URL + "&appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
list_temp = response['main']['temp']

weather = []
current_time = dt.datetime.now()
for i in range(7):
    current_temp = {}
    current_temp['date'] = current_time + dt.timedelta(days=i-7)
    current_temp['temp'] = list_temp
    weather.append(current_temp)
    conv = list_temp - 273.15
    conv = round(conv, 2)
    print(f"{current_time + dt.timedelta(days=i-7)}: {conv}°C")

temperatures = [ conv for day in weather]
print(CITY)
print(temperatures)

