# app/main.py
import os
import requests


def get_weather(api_key: str) -> None:
    url = (
        f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    )
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for 4xx/5xx status codes
    data = response.json()
    print(f"Weather in Paris: {data['current']['condition']['text']}, {data['current']['temp_c']}°C")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable is missing.")
        exit(1)
    get_weather(api_key)
