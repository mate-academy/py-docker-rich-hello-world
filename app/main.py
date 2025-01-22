import os
import requests

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise KeyError("API_KEY not provided")
url = "http://api.weatherapi.com/v1/current.json"
CITY = "San Francisco"


def get_weather(city: str) -> dict | None:
    params = {"key": API_KEY, "q": city}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


# Main function
if __name__ == "__main__":
    weather_data = get_weather(CITY)
    if weather_data:
        print(
            f"{CITY}: {weather_data['current']['condition']['text']}, "
            f"Temperature: {weather_data['current']['temp_c']}°C"
        )
    else:
        print("Failed to retrieve weather data.")
