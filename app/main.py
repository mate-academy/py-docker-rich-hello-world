import os

import requests


def get_weather(city: str = "Paris") -> None:
    print(f"Performing request to Weather API for city {city}...")
    url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}&q={city}"
    response = (requests.get(url)).json()
    print(
        f"{response["location"]["name"]}/{response["location"]["country"]} "
        f"{response["location"]["localtime"]} "
        f"Weather: {response["current"]["temp_c"]} Celsius, "
        f"{response["current"]["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
