import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        weather_data = response.json()

        location = weather_data["location"]["tz_id"]
        local_time = weather_data["location"]["localtime"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        print(
            f"{location} {local_time} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    get_weather()
