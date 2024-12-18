import os

import dotenv
import requests


CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    key = os.getenv("API_KEY")
    if not key:
        print("No API key provided")
        return
    request = requests.get(
        URL,
        params={"key": key, "q": CITY},
    )
    if request.status_code == 200:
        data = request.json()["current"]
        time = data.get("last_updated")
        temperature = data.get("temp_c")
        weather = data.get("condition").get("text")
        print(f"Paris/France {time} Weather: {temperature} Celsius, {weather}")
    else:
        print("Error")
        print(request)
        print(request.text)


if __name__ == "__main__":
    dotenv.load_dotenv()
    get_weather()
