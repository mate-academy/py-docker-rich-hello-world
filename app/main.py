import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    try:
        response = requests.get(
            f"{BASE_URL}?key={API_KEY}&q={FILTERING}"
        )
        response.raise_for_status()

        data = response.json()

        name = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temper = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]

        print(f"{name}/{country} {localtime}"
              f"Weather: {temper} Celsium, {weather}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP Error: {e}")
    except KeyError as e:
        print(f"Missing data in response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()
