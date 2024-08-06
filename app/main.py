import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    try:
        print(f"Start request to Weather API for city {CITY}...")
        res = requests.get(URL, params={"key": API_KEY, "q": CITY})
        res.raise_for_status()

        try:
            data = res.json()
            location_name = data["location"]["name"]
            country = data["location"]["country"]
            local_time = data["location"]["localtime"]
            temp_c = data["current"]["temp_c"]
            weather = data["current"]["condition"]["text"]

            print(
                f"{location_name}/{country} "
                f"{local_time} Weather: {temp_c} Celsius, {weather}"
            )
        except ValueError:
            print("Failed to parse JSON response.")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Missing key in response data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
