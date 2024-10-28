def input_temperature():
    while True:
        try:
            value = float(input("Enter the temperature in Celsius: "))
            return value
        except ValueError:
            print("Please enter a valid number.")

def convert_temperature(temp):
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (temp * 9/5) + 32
    # Convert Celsius to Reamur
    reamur = temp * 4/5
    # Convert Celsius to Kelvin
    kelvin = temp + 273.15
    return fahrenheit, reamur, kelvin

# Main execution
if __name__ == "__main__":
    temperature = input_temperature()  # Call the first function
    fahrenheit, reamur, kelvin = convert_temperature(temperature)  # Get all conversions
    # print(f"The converted temperatures are:")
    # print(f"{fahrenheit:.2f} °F")
    # print(f"{reamur:.2f} °R")
    # print(f"{kelvin:.2f} K")


Jawa_timur = {
           
    "Surabaya" : {
        "Province": "Jawa Timur",
        "temp_7d": [27.4, 26.4, 27.1, 25.3, 26.5, 26.4, 26.1],
        "ave_temp": sum([27.4, 26.4, 27.1, 25.3, 26.5, 26.4, 26.1])/7,
        "coordinates": {112.62, -7.26},
                },

    "Mojokerto" : {
        "Province": "Jawa Timur",
        "temp_7d": [26.4, 25.5, 26.5, 25.2, 26.2, 25.2, 25.3],
        "ave_temp": sum([26.4, 25.5, 26.5, 25.2, 26.2, 25.2, 25.3])/7,
        "coordinates": { -7.470211991329571, 112.440603926822}
    },

    "Gresik" : {
        "Province": "Jawa Timur",
        "temp_7d": [27.1, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5],
        "ave_temp": sum([27.1, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5])/7,
        "coordinates": {112.62, -7.26}
    },

    "Pasuruan" : {
        "Province": "Jawa Timur",
        "temp_7d": [27.4,25.4, 26.1, 26.3, 26.5, 27.1, 27.2],
        "ave_temp": sum([27.4,25.4, 26.1, 26.3, 26.5, 27.1, 27.2])/7,
        "coordinates": {112.62, -7.26}
    },

    "Jombang" : {
        "Province": "Jawa Timur",
        "temp_7d": [26.0,25.5, 26.5,27.1, 26.5, 26.5, 25.7],
        "ave_temp": sum([26.0,25.5, 26.5,27.1, 26.5, 26.5, 25.7])/7,
        "coordinates": {112.62, -7.26}
    },

    "Malang" : {
        "Province": "Jawa Timur",
        "temp_7d": [23.1, 22.4, 24.5, 24.3, 23.6, 25.3, 24.6],
        "ave_temp": sum([23.1, 22.4, 24.5, 24.3, 23.6, 25.3, 24.6])/7,
        "coordinates": {112.62, -7.26}
    },

    "Banyuwangi" : {
        "Province": "Jawa Timur",
        "temp_7d": [26.7, 26.5, 26.5, 26.7, 26.5, 26.1, 26.3],
        "ave_temp": sum([26.7, 26.5, 26.5, 26.7, 26.5, 26.1, 26.3])/7,
        "coordinates": {112.62, -7.26}
    },

    "Madiun" : {
        "Province": "Jawa Timur",
        "temp_7d": [25.9, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5],
        "ave_temp": 25.9,
        "coordinates": {112.62, -7.26}
    },

    "Nganjuk" : {
        "Province": "Jawa Timur",
        "temp_7d": [27.5, 25.4, 26.5, 26.3, 26.5, 26.3, 26.5],
        "ave_temp": 26.7,
        "coordinates": {112.62, -7.26}
    },

    "Blitar" : {
        "Province": "Jawa Timur",
        "temp_7d": [26.5, 25.5, 26.5, 25.2, 26.2, 25.2, 25.3],
        "ave_temp": 26.3,
        "coordinates": {112.62, -7.26}
    }
}

def convert_temperatures(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9/5) + 32
    return kelvin, fahrenheit

# Suhu dari 5 kota
city_temperatures = {
    'Jakarta': 30.0,
    'Bandung': 25.0,
    'Surabaya': 32.0,
    'Medan': 28.0,
    'Bali': 27.0
}

# Menampilkan daftar kota
print("Daftar Kota:")
for index, city in enumerate(city_temperatures.keys(), start=1):
    print(f"{index}. {city}")

# Memilih kota untuk dikonversi
choice = int(input("Pilih nomor kota untuk konversi suhu (1-5): "))
selected_city = list(city_temperatures.keys())[choice - 1]
suhu_celsius = city_temperatures[selected_city]

# Melakukan konversi suhu
kelvin, fahrenheit = convert_temperatures(suhu_celsius)

# Menampilkan hasil konversi
print(selected_city)
print(f"\nHasil Konversi Suhu di {selected_city}:")
print(f"  Suhu dalam Kelvin: {kelvin:.2f} K")
print(f"  Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")

angka = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# Menampilkan pilihan menu
print("Pilih salah satu angka dari daftar berikut:")
for i, num in enumerate(angka):
    print(f"{i + 1}. {num}")

# Meminta input dari pengguna untuk memilih indeks
pilihan = int(input("Masukkan nomor pilihan (1-10): ")) - 1

# Memastikan input valid
if 0 <= pilihan < len(angka):
    print(f"Anda memilih angka: {angka[pilihan]}")
else:
    print("Pilihan tidak valid.")