import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    url = f"{URL}?key={API_KEY}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        current_time = data["location"]["localtime"]
        temp_celsius = data["current"]["temp_c"]
        current_weather = data["current"]["condition"]["text"]

        weather_condition_1st_line = (
            f"Performing request to weather API for city {city}...")
        weather_condition_2nd_line = (
             f"{city}/{country} {current_time} "
             f"Weather: {temp_celsius} "
             f"Celsius, {current_weather}"
        )

        print(weather_condition_1st_line)
        print(weather_condition_2nd_line)
    else:
        error_message = (
            response.json().get("error", {})
            .get("message", "Unknown error occurred")
        )
        print("Error:", error_message)


if __name__ == "__main__":
    get_weather()
