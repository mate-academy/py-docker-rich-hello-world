import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data: {response.text}")

    data = response.json()

    location = data.get("location", {})
    current = data.get("current", {})

    print("Weather information for Paris:")
    print(f"City: {location.get('name', 'Unknown')}")
    print(f"Region: {location.get('region', 'Unknown')}")
    print(f"Country: {location.get('country', 'Unknown')}")
    print(f"Temperature: {current.get('temp_c', 'Unknown')}°C")
    print(f"Condition: {current.get('condition', {}).get('text', 'Unknown')}")
    print(f"Wind: {current.get('wind_kph', 'Unknown')} kph, Direction: {current.get('wind_dir', 'Unknown')}")
    print(f"Humidity: {current.get('humidity', 'Unknown')}%")
    print(f"Cloud Cover: {current.get('cloud', 'Unknown')}%")
    print(f"Visibility: {current.get('vis_km', 'Unknown')} km")


if __name__ == "__main__":
    get_weather()
