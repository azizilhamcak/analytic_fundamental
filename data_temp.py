import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "cec1de6786fa2cdfdd123c10c3407749"
CITY = input("Enter city name: ")

url = f"{BASE_URL}q={CITY}&appid={API_KEY}"

response = requests.get(url).json()


weather = []
current_time = dt.datetime.now()
for i in range(7):
    forecast = response['list'][i]
    date = forecast['dt_txt']
    dates = current_time + dt.timedelta(days=i)
    list_temp = forecast['main']['temp']
    conv = list_temp - 273.15
    conv = round(conv, 2)
    
    current_temp = {
        'date': dates,
        'temp': conv
    }

    weather.append(current_temp)
    print(f"{current_temp['date']} : {current_temp['temp']}°C")

temperatures = [ day['temp'] for day in weather]
print(CITY)
print(temperatures)

