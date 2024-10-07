import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY is not set!")
        return
    params = {
        "key": API_KEY,
        "q": CITY
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            print("Performing request to Weather API for city Paris...")
            print(
                f"Paris/France {data["location"]["localtime"]} Weather: "
                f"{data["current"]["temp_c"]} Celsius, "
                f"{data["current"]["condition"]["text"]}"
            )
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON, response text:", response.text)
    else:
        print(
            f"Failed to get weather data: {response.status_code}, "
            f"response text: {response.text}"
        )


if __name__ == "__main__":
    get_weather()
