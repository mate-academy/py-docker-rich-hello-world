import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"

print(f"API_KEY: {API_KEY}")


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("No API key provided")

    params = {
        "key": API_KEY,
        "q": CITY,
    }

    print(f"Request URL: {BASE_URL}")
    print(f"Request parameters: {params}")

    response = requests.get(BASE_URL, params=params)

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")

    if response.status_code == 200:
        weather_data = response.json()
        print(
            f"Current weather in Paris: {weather_data['current']['temp_c']}°C"
        )
    else:
        print(
            f"Failed to get weather data: {response.status_code} - "
            f"{response.json().get('error', {}).get(
                'message', 'No error message'
            )}"
        )


if __name__ == "__main__":
    get_weather()
