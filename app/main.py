import os
import requests

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json?"


def get_weather(city: str) -> None:
    if not API_KEY:
        raise ValueError("No API key provided. Set the API_KEY environment variable.")

    response = requests.get(BASE_URL, params={"key": API_KEY, "q": city})

    if response.status_code == 200:
        data = response.json()
        print(f"Performing request to Weather API for city {city}...")
        print(
            f"{city}/{data['location']['country']} {data['location']['localtime']} Weather: {data['current']['temp_c']}°C, {data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather(city="Paris")
