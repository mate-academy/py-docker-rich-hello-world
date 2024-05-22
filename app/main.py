import json
import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_str_from_dict(response_data: dict) -> str:
    location = response_data.get("location")
    country = location.get("country")
    city = location.get("name")
    time = location.get("localtime")

    current_info = response_data.get("current")
    temp_c = current_info.get("temp_c")
    condition = current_info.get("condition").get("text")

    return f"{city}/{country} {time} Weather: {temp_c} Celsius, {condition}"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")

    payload = {
        "q": FILTERING,
        "key": API_KEY
    }
    response = requests.get(URL, params=payload)
    response_data = json.loads(response.content)

    try:
        print(get_str_from_dict(response_data))
    except Exception as e:
        print(
            f"An error occurred: {e}"
        )


if __name__ == "__main__":
    get_weather()
