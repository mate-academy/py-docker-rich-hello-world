import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"

API_KEY = os.getenv("API_KEY")

PARAMS = {
    "key": API_KEY,
    "q": "Paris",
}

def get_res():
    try:
        print("Performing request to Weather API to city Paris...")
        response = requests.get(URL, params=PARAMS)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP ERROR: {err}")
    except requests.exceptions.RequestException as err:
        print(f"REQUEST ERROR: {err}")
    return response.json()

def get_weather() -> None:
    weather = get_res()

    location = weather["location"]["name"]
    country = weather["location"]["country"]
    temperature = weather["current"]["temp_c"]
    date_time = weather["location"]["localtime"]
    condition = weather["current"]["condition"]["text"]
    print(
        f"{location}/{country} {date_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
