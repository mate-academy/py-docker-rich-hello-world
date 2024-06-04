import os

import requests

API_KEY = os.environ.get("API_KEY")
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    request = requests.get(
        WEATHER_API_URL,
        params={"key": API_KEY, "q": "France"}
    )

    if request.status_code != 200:
        print("Error: Can't get data from Weather API.")
        return

    request = request.json()
    print(
        f"{request['location']['name']}/{request['location']['country']} "
        f"{request['current']['last_updated']} "
        f"Weather: {request['current']['temp_c']} Celsius, "
        f"{request['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
