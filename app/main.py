import requests
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    key = api_key
    default_city = "Kyiv"

    try:
        params = {
            "q": default_city,
            "key": key,
            "aqi": "no"
        }
        response = requests.get(url, params=params)
    except ValueError:
        print("ERROR: API_KEY is not correct or invalid.")

    try:
        weather_data = response.json()
        print(f"Current weather in {weather_data['location']['name']}:\n",
        f"Temperature: {weather_data['current']['temp_c']}°C\n",
        f"Weather: {weather_data['current']['condition']['text']}\n")
    except ValueError:
        print("ERROR: Connection failed.")


if __name__ == "__main__":
    get_weather()
