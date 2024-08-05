import os
import requests


URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    url = f"{URL}key={api_key}&q={CITY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"Current weather in Paris: {data['current']['condition']['text']}, {data['current']['temp_c']}°C")
    else:
        print(f"Error: {data['error']['message']}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if api_key:
        get_weather(api_key)
    else:
        print("API_KEY not found. Please set it as an environment variable.")
