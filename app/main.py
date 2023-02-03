import os

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json?key="
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"

URL = BASE_URL + API_KEY + "&q=" + CITY


def get_weather() -> None:
    response = requests.get(URL).json()
    print(
        f"Country: {response['location']['country']}.\n"
        f"City: {response['location']['name']}.\n"
        f"Time zone: {response['location']['tz_id']}.\n"
        f"Current time: {response['location']['localtime']}.\n"
        f"Temperature: {response['current']['temp_c']} °C.\n"
        f"Wind speed: {response['current']['wind_mph']} m/h."
    )


if __name__ == "__main__":
    get_weather()
