import os
import requests

API_KEY = os.getenv("API_KEY")
url = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> dict | None:
    params = {"key": API_KEY, "q": city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Main function
if __name__ == "__main__":
    city = "San Francisco"
    weather_data = get_weather(city)
    if weather_data:
        print(
            f"{city}: {weather_data['current']['condition']['text']}, "
            f"Temperature: {weather_data['current']['temp_c']}°C"
        )
    else:
        print("Failed to retrieve weather data.")
