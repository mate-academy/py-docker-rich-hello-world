import os

import requests


def fetch_weather_data() -> dict:
    """
    Fetches current weather data from the API for specified city.
    """
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    city = os.getenv("CITY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {"key": api_key, "q": city}

    try:
        weather_response = requests.get(api_url, params=params)
        weather_response.raise_for_status()
        return weather_response.json()
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Failed to fetch weather data: {str(error)}")


def display_weather_info(weather_data: dict) -> None:
    """
    Displays formatted weather information in the console.
    """
    try:
        location = weather_data["location"]
        city = location["name"]
        country = location["country"]
        local_time = location["localtime"]

        current_weather = weather_data["current"]
        current_temperature = current_weather["temp_c"]
        current_conditions = current_weather["condition"]["text"]

        print(f"Performing request to Weather API for city {city}...")
        print(
            f"{city}/{country} {local_time} Weather: "
            f"{current_temperature} Celsius, {current_conditions}"
        )
    except KeyError as error:
        raise ValueError(f"Invalid weather data format: missing {str(error)}")


def get_weather() -> None:
    """
    Fetches current weather data for specified
    city and displays it in the console.
    """
    weather_data = fetch_weather_data()
    display_weather_info(weather_data)


if __name__ == "__main__":
    get_weather()
