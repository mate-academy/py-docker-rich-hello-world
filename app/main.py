import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


def get_weather(city: str) -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError(
            "API_KEY is not set. Please provide it as an environment variable"
        )

    url = f"{BASE_URL}?key={api_key}&q={DEFAULT_CITY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Perform request to Weather API for city {DEFAULT_CITY}...")

        city = data["location"]["name"]
        country = data["location"]["country"]
        datetime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{city}/{country} {datetime} "
              f"Weather: {temperature} {condition}")
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    get_weather(DEFAULT_CITY)
