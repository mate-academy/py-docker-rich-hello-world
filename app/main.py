import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API_KEY environment variable not set")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Current weather in {city}: {temperature}°C, {condition}")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
