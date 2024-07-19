import requests
import os

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
        }
    )

    if response.status_code == 200:
        data = response.json()
        print(
            f"Performing request to Weather API for city {CITY}...\n"
            f"{data['location']['name']}/{data['location']['country']}, "
            f"{data['current']['last_updated']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}."
        )
    else:
        print(f"Can't get data from Weather API. "
              f"Status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
