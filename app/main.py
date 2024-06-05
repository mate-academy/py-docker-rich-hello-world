import os
import requests


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if API_KEY is None:
        raise ValueError("API_KEY environment variable is not set")
    payload = {
        "key": API_KEY,
        "q": FILTERING,
    }
    result = requests.get(URL, params=payload)
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
