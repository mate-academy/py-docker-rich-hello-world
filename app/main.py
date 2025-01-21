import os
import requests
import sys


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY environment variable not set.",
              file=sys.stderr)
        sys.exit(1)

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {location}, {country}: {temp_c}°C, {condition}")
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching or parsing weather data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
