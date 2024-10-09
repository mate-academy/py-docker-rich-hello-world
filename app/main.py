import os
import requests


def get_weather(api_key: str) -> None:
    base_url = "http://api.weatherapi.com/v1/current.json?"
    location = "Paris"
    params = f"key={api_key}&q={location}"

    url = base_url + params
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Current weather in Paris: {data['current']['temp_c']}°C")
    else:
        print("Failed to get weather data", response.status_code)


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    get_weather(api_key)
