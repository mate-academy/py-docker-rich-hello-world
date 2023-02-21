from os import getenv

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    url = f"{URL}key={API_KEY}&q={FILTERING}&aqi=yes"
    response = requests.get(url)
    response = response.json()
    location = response["location"]
    current = response["current"]
    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} "
          f"Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
