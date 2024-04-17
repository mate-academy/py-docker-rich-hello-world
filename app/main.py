import os
import requests


API_KEY = os.environ.get("OPENWEATHER_API_KEY")
URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather() -> None:
    params = {"q": "Paris", "appid": API_KEY, "units": "metric"}

    if not API_KEY:
        raise ValueError(
            "API key not found. Please set the "
            "OPENWEATHER_API_KEY environment variable."
        )

    try:
        response = requests.get(URL, params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"Weather in Paris:\n"
                  f"Description: {weather_description}\n"
                  f"Temperature: {temperature}°C\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s")
        else:
            print("Failed to retrieve weather data.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
