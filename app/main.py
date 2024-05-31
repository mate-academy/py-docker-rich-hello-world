import os

import requests

CITY = "Paris"
API_KEY = os.environ.get("API_KEY")
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    response = requests.get(URL)

    if response.status_code == 200:
        valid_response = response.json()
        city_name = valid_response["location"]["name"]
        country_name = valid_response["location"]["country"]
        location = valid_response["location"]["localtime"]
        temperature = valid_response["current"]["temp_c"]
        condition_text = valid_response["current"]["condition"]["text"]
        print(
            f"Performing request to Weather API for city {city_name}...\n"
            f"{city_name}/{country_name} {location} "
            f"Weather: {temperature} Celsius, {condition_text}"
        )
    else:
        print("Response is invalid!")


if __name__ == "__main__":
    get_weather()
