import os
import requests


API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    try:
        print(f"Start request to Weather API for city {FILTERING}...")
        res = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
        res.raise_for_status()
        data = res.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_celsius = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} "
            f"{local_time} Weather: {temp_celsius} Celsius, {weather}"
        )
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Missing key in the response data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
