import datetime as dt
import requests 
from pprint import PrettyPrinter

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "38a6e22754d5b0436b0e265fecb8ec98"

CITY = "Ndanai"
printer = PrettyPrinter()

# a function that converts kelvin to selsius
def kelvin_to_celsius(kelvin):
	selsius = kelvin -273.5
	return selsius

# A function that converts m/s to km/h
def convert_speed(m_per_sec):
	km_per_h = m_per_sec*3.6
	return km_per_h

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
# printer.pprint(response)

temp_kelvin = response['main']['temp']
temp_selsius = kelvin_to_celsius(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)


humidity = response['main']['humidity']
weather_desc = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

wind_speed_in_ms = response['wind']['speed']
wind_speed = convert_speed(wind_speed_in_ms)


print(f"Today's wind speed in {CITY} is: {wind_speed}km/h\n")
print(f"The temperature for today in {CITY} is: {temp_selsius}degrees selsius...")
if feels_like_celsius > 24:
	print("So it is fairly hot today, dress lightly")
else:
	print("So it is gonna be cold, carry a sweater!\n")
print(f"It feels like: {feels_like_celsius} today in {CITY}\n")
print(f"Today's humidity reads: {humidity} in {CITY} today\n")
print(f"Today's weather in {CITY} today is: {weather_desc}\n")
print(f"The sun rises today in {CITY} at: {sunrise_time}\n")
print(f"The sun sets today in {CITY} at: {sunset_time}")  

