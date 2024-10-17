import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)

URL = "http://api.weatherapi.com/v1"
CITY = "Paris"


def get_weather(CITY, api_key):
    complete_url = f"{URL}/current.json?key={api_key}&q={CITY}"
    response = requests.get(complete_url)
    data = response.json()
    return data


if __name__ == "__main__":
    weather_data = get_weather(CITY, api_key)

    print(f"Weather in: {CITY}")
    print(f"Temperature: {weather_data["current"]["temp_c"]} °C")
    print(f"Condition: {weather_data["current"]["condition"]["text"]}")
