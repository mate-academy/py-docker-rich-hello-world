import os
import requests

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    request = requests.get(URL + f"key={api_key}&q={FILTERING}").json()

    temp = request["current"]["temp_c"]
    cond = request["current"]["condition"]["text"]

    print(f"{FILTERING}, weather: {temp} Celsius, {cond}")


if __name__ == "__main__":
    get_weather()
