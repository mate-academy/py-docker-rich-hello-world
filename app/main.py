import os
import requests


def get_weather(api_key: str, city: str = "Paris") -> None:
    url = (
        f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        try:
            weather_data = response.json()
            try:
                print(
                    f"{weather_data['location']['name']}/"
                    f"{weather_data['location']['country']} "
                    f"{weather_data['location']['localtime_epoch']} "
                    f"Temperature: {weather_data['current']['temp_c']} "
                    f"Celsius, {weather_data['current']['condition']['text']}"
                )
            except KeyError as e:
                print(f"Missing key in the response data: {e}")
        except ValueError:
            print("Error parsing the response JSON.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data: {e}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        get_weather(api_key)
