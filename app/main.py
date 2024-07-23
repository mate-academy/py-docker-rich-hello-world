import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    url = f"{URL}?key={API_KEY}&q={CITY}"
    response = requests.get(url).json()
    print(response)

    city = response["location"]["name"]
    country = response["location"]["country"]
    current_time = response["location"]["localtime"]
    temp_celsius = response["current"]["temp_c"]
    current_weather = response["current"]["condition"]["text"]

    weather_condition_1st_line = (
        f"Performing request to weather API for city {city}...")
    weather_condition_2nd_line = (
        f"{city}/{country} {current_time} "
        f"Weather: {temp_celsius} "
        f"Celsius, {current_weather}"
    )

    if "error" in response:
        print("Error:", response["error"]["message"])
    else:
        print(weather_condition_1st_line)
        print(weather_condition_2nd_line)


if __name__ == "__main__":
    get_weather()
