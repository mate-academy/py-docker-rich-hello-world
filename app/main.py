import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&aqi=no"


def get_weather() -> None:
    weather = requests.get(URL)
    if weather.status_code == 200:
        weather = weather.json()
        print(
            f"{weather['location']['name']}/{weather['location']['country']}",
            weather["current"]["last_updated"],
            "Weather:",
            weather["current"]["temp_c"],
            "Celsius,",
            weather["current"]["condition"]["text"]
        )
    else:
        weather.raise_for_status()


if __name__ == "__main__":
    get_weather()
