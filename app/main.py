import os

import requests


URL = "https://api.weatherapi.com/v1/current.json?"

FILTERING = "Ile-de-France"


def get_weather() -> None:

    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY is not set in environment variables")
        return

    response = requests.get(
        URL + "key=" + api_key + "&q=" + FILTERING + "&aqi=yes"
    )
    if response.status_code == 200:
        data = response.json()
        print(f"{data['location']['name']}/{data['location']['country']} "
              f"{data['current']['last_updated']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
