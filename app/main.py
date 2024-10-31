# app/main.py
import os
import requests

# Define API base URL as a constant
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(api_key: str) -> None:
    url = f"{WEATHER_API_URL}?key={api_key}&q=Paris"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"Weather in Paris: {data['current']['condition']['text']},"
          f" {data['current']['temp_c']}°C")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable is missing.")
        exit(1)
    get_weather(api_key)
