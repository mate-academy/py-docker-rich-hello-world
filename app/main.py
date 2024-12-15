import requests
from dotenv import load_dotenv
import os

load_dotenv()


def get_weather() -> dict:
    URL = "http://api.weatherapi.com/v1/current.json"
    CITY = "Paris"
    res = requests.get(f"{URL}?key={os.getenv("API_KEY")}&q={CITY}")
    city = res.json()["location"]["name"]
    country = res.json()["location"]["country"]
    date = res.json()["location"]["localtime"]
    temp_c = res.json()["current"]["temp_c"]
    if res.json()["current"]["cloud"] > 50:
        weather = "Cloudy"
    else:
        weather = "Sunny"
    return f"{city}/{country} {date}, Wether: {temp_c} Celsius, {weather}"


if __name__ == "__main__":
    print(get_weather())
