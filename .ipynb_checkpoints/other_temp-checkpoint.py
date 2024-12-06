import requests
from datetime import datetime, timedelta

# Ganti dengan API key Anda
API_KEY = 'cec1de6786fa2cdfdd123c10c3407749'
# Ganti dengan nama kota atau koordinat yang diinginkan
CITY =  input("Masukkan kota atau koordinat: ")
# URL untuk API
URL = 'http://api.openweathermap.org/data/2.5/onecall/timemachine'

# Fungsi untuk mendapatkan data temperatur
def get_historical_weather(city, api_key):
    # Ambil data koordinat kota
    geo_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(geo_url)
    data = response.json()
   

   
    temperatures = []
   
    # Ambil data untuk 7 hari terakhir
    for days_ago in range(1, 8):
        timestamp = int((datetime.now() - timedelta(days=days_ago)).timestamp())
        params = {
            'dt': timestamp,
            'appid': api_key,
            'units': 'metric'  # Gunakan 'imperial' untuk Fahrenheit
        }
        response = requests.get(URL, params=params)
        historical_data = response.json()
       
        if 'current' in historical_data:
            temperature = historical_data['current']['temp']
            temperatures.append((days_ago, temperature))
        #else:
         #   print(f"Error retrieving data for {days_ago} days ago: {historical_data.get('message')}")
   

# # Panggil fungsi dan cetak hasilnya
temperatures = get_historical_weather(CITY, API_KEY)
for day, temp in temperatures:
     print(f'Temperature {day} days ago: {temp} °C')