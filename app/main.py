import os
import requests
from requests import Response


def get_weather(api_key: str, city: str = "Paris") -> None:
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['location']['name']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        exit(1)
    get_weather(api_key)
