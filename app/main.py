import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("No API_KEY found in environment variables")

    city = "Paris"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data["current"]
        print(
            f"Current weather in {city}:"
            f" {weather['condition']['text']}, {weather['temp_c']}°C"
        )
    else:
        print(
            f"Failed to get weather data: "
            f"{data.get('error', {}).get('message', 'Unknown error')}"
        )


if __name__ == "__main__":
    get_weather()
