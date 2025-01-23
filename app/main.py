import os

import requests
from dotenv import load_dotenv


def get_weather() -> None:
    print("Performing request to Weather api for Paris...")

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = (f"https://api.weatherapi.com/v1/current."
           f"json?key={api_key}&q=Paris&aqi=no")
    res = requests.get(url)
    res_data = res.json()

    city = res_data["location"]["name"]
    country = res_data["location"]["country"]
    time = res_data["location"]["localtime"]
    temperature = res_data["current"]["temp_c"]
    condition = res_data["current"]["condition"]["text"]

    weather_msg = (f"{city}/{country} {time} "
                   f"Weather: {temperature} Celsius, {condition}")

    print(weather_msg)


if __name__ == "__main__":
    get_weather()
