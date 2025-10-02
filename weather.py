# 
import requests

city = input("Enter city name: ")
api_key = "YOUR_API_KEY"  # Get one free from OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url).json()

if response.get("cod") != 200:
    print("City not found ❌")
else:
    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    print(f"🌤️ Weather in {city}: {temp}°C, {desc}")
