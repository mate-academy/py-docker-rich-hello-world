import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
params = {"key": API_KEY, "q": "Paris"}


def get_weather() -> None:
    try:
        res = requests.get(BASE_URL, params=params)
        res.raise_for_status()
        data = res.json()

        location_name = data["location"]["name"]
        location_country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition_text = data["current"]["condition"]["text"]

        print(f"{location_name}/{location_country}")
        print(f"{localtime}")
        print(f"Weather: {temp_c} Celsius, {condition_text}")

    except requests.RequestException as e:
        print(f"Network or HTTP error occurred: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    except KeyError as e:
        print(f"Missing expected key in the response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
