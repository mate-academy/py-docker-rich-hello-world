import requests
import os

BASE_URL = "http://api.weatherapi.com/v1/current.json"
city = "Paris"


def get_weather(api_key: str) -> None:
    weather_paris_url = f"{BASE_URL}?key={api_key}&q={city}"
    try:
        response = requests.get(weather_paris_url)
    except requests.exceptions.ConnectionError:
        print("Connection Error")

    weather = response.json()

    if response.status_code == 200:
        print(
            f"{weather["location"]["name"]}/"
            f"{weather["location"]["country"]} "
            f"{weather["location"]["localtime"]} "
            f"Weather: {weather["current"]["temp_c"]} "
            f"Celsius, {weather["current"]["condition"]["text"]}"
        )
    else:
        "There is no data about weather"


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    get_weather(api_key)
