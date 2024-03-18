import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather(city: str) -> None:
    print(f"Performing request to Weather API for city {city}...")
    result = requests.get(
        URL,
        params={"key": API_KEY, "q": city}
    )

    if result.status_code != 200:
        raise Exception("Somthing went wrong...")

    location = result["location"]
    current = result["current"]

    city = location["name"] + "/" + location["country"]
    localtime = location["localtime"]
    temp_c = current["temp_c"]
    condition = current["condition"]["text"]

    print(f"{city} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather("Paris")
