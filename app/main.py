import os
import requests


def get_weather(api_key: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Weather report for {location}: {temp_c}°C, {condition}"
    else:
        return "Failed to get weather data"


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
    print(get_weather(api_key))
