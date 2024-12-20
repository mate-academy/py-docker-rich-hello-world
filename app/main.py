import os

import requests


def get_weather(api_key: str) -> None:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['location']['name']}")
        print(f"Country: {data['location']['country']}")
        print(f"Temp: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable is missing.")
    else:
        get_weather(api_key)
