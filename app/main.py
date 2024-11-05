import os
import requests


API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    payload = {
        "key": API_KEY,
        "q": FILTERING,
    }
    res = requests.get(BASE_URL + "/current.json", params=payload)
    data = res.json()
    location = data["location"]
    current = data["current"]
    print("Performing request to Weather API for city Paris...")
    print(f"{location["name"]}/{location["country"]} \
          {location["localtime"]} Weather: {current["temp_c"]} \
            Celsius, {current["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
