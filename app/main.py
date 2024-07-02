import os

import requests


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("No API_KEY set for the application")
    try:
        result = requests.get(URL + f"key={API_KEY}&q={FILTERING}&aqi=no")
        result.raise_for_status()
        data = result.json()
        print(
            data["location"]["name"]
            + "/"
            + data["location"]["country"]
            + " "
            + data["location"]["localtime"]
            + " Weather: "
            + str(data["current"]["temp_c"])
            + " Celsius, "
            + data["current"]["condition"]["text"]
        )
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    get_weather()
