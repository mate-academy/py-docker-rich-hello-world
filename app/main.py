import os
import requests


API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    params = {
        "key": api_key,
        "q": CITY
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        location_time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition_text = data["current"]["condition"]["text"]
        location = data["location"]["name"]
        country = data["location"]["country"]
        print(
            f"{location}/{country} {location_time} Weather: "
            f"{temperature} Celsius, "
            f"{condition_text}"
        )
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if api_key:
        get_weather(api_key)
    else:
        print("API_KEY not found. Please set the environment variable.")
