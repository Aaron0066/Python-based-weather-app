
import requests

api_key = "60b9e1f6f930bc091153df32ff0088b0"

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code == 404:
    print("No city detected")

else:
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")























