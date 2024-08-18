import requests
import os


KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    try:
        params = {
            "q": "Kyiv",
            "key": KEY,
            "aqi": "no"
        }
        response = requests.get(URL, params=params)
    except ValueError:
        print("ERROR: API_KEY is not correct or invalid.")

    try:
        weather_data = response.json()
        print(
            f"Current weather in {weather_data['location']['name']}:\n",
            f"Temperature: {weather_data['current']['temp_c']}°C\n",
            f"Weather: {weather_data['current']['condition']['text']}\n"
        )
    except ValueError:
        print("ERROR: Connection failed.")


if __name__ == "__main__":
    get_weather()
