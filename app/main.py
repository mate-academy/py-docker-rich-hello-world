import os

import requests


def get_weather(city: str, key: str) -> None:
    """
        Get weather information for a given city using the WeatherAPI.

        :param city: The name of the city to get weather information for.
        :param key: The API key required to access the WeatherAPI.
    """
    if not city:
        raise ValueError("City parameter is required")
    if not key:
        raise ValueError("API key is required")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": key,
        "q": city,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    daytime = "day" if data["current"]["is_day"] else "night"
    wind_direction = {
        "N": "North",
        "NE": "Northeast",
        "E": "East",
        "SE": "Southeast",
        "S": "South",
        "SW": "Southwest",
        "W": "West",
        "NW": "Northwest"
    }.get(data["current"]["wind_dir"])

    print(f"Welcome to {data["location"]["name"]}, "
          f"{data["location"]["country"]}!\n"
          f"Today is {data["location"]["localtime"]} and it is {daytime}.\n"
          f"The current temperature is {data["current"]["temp_c"]}°C "
          f"({data["current"]["temp_f"]}°F) with "
          f"{data["current"]["condition"]["text"].lower()} conditions.\n"
          f"The wind speed is {data["current"]["wind_kph"]} kph coming "
          f"from the {wind_direction} direction.\n"
          f"The humidity is {data["current"]["humidity"]}% and the "
          f"visibility is {data["current"]["vis_km"]} kilometers.\n"
          f"Have a good {daytime}!")


if __name__ == "__main__":
    city_name = os.environ.get("CITY", "London")
    api_key = os.environ.get("API_KEY")
    get_weather(city_name, api_key)
