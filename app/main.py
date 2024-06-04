import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("No API key provided")

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current weather in Paris: "
              f" {weather_data["current"]["temp_c"]}°C")
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    get_weather()
