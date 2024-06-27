import os
import requests

URL = "http://api.weatherapi.com/v1/forecast.json?"
FILTERING = "Paris"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:

    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    data = result.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]
    print(f"{city}/{country} {time} Weather: {temperature} Celsius {weather}")


if __name__ == "__main__":
    get_weather()
