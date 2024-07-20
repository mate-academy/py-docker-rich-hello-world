import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(api_key: str, city: str, url: str) -> str:
    params = {"key": api_key, "q": city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Temperature in {location}: {temp_c}°C, {condition}"
    else:
        return f"Status code: {response.status_code}"


if __name__ == "__main__":
    print(get_weather(API_KEY, CITY, URL))
