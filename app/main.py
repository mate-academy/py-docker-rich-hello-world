import os
import requests


API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    if API_KEY is not None:
        payload = {
            "key": API_KEY,
            "q": FILTERING,
        }
        res = requests.get(BASE_URL + "/current.json", params=payload)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error: {err}")
            return
        data = res.json()
        location = data.get("location")
        current = data.get("current")
        if location is not None or current is not None:
            print("Performing request to Weather API for city Paris...")
            print(f"{location['name']}/{location['country']} "
                  f"{location['localtime']} Weather: {current['temp_c']} "
                  f"Celsius, {current['condition']['text']}")
        else:
            print("Error: Invalid response from Weather API")
            return
    else:
        print("Error: WEATHER_API_KEY is not set. \
                  Please set the environment variable and try again.")
        return


if __name__ == "__main__":
    get_weather()
