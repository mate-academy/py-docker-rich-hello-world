import os

import requests

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    request = requests.get(URL, params={"key": API_KEY, "q": FILTERING})

    if request.status_code != 200:
        print(f"Error: {request.status_code}")
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
