import os
import requests


def get_weather(api_key: None, city: str = "Paris") -> None:
    url = (
        f"http://api.weathe"
        f"rapi.com/v1/current.json?key={api_key}&q={city}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        print(
            f"{weather_data['location']['name']}/"
            f"{weather_data['location']['country']} "
            f"{weather_data['location']['localtime_epoch']} "
            f"Temperature: {weather_data['current']['temp_c']} "
            f"Celsius, {weather_data['current']['condition']['text']}"
        )
    else:
        print(f"Failed to get weather data: {response.status_code}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        get_weather(api_key)
