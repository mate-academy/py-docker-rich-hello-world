import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY not found in environment variables.")
        return

    city = "Paris"
    url = (
        f"http://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q={city}&aqi=yes"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]

        print(
            f"Location: {location['name']}, "
            f"{location['region']}, "
            f"{location['country']}"
        )
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Wind: {current['wind_kph']} kph from the "
              f"{current['wind_dir']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Last updated: {current['last_updated']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    get_weather()
