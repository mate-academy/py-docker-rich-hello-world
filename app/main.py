import os
import requests
import logging


WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_weather_data(api_key: str, city: str) -> dict:
    try:
        response = requests.get(
            WEATHER_API_URL, params={"key": api_key, "q": city}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
        return {}


def display_weather_info(data: dict) -> None:
    if data:
        location_time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition_text = data["current"]["condition"]["text"]
        location = data["location"]["name"]
        country = data["location"]["country"]
        logging.info(
            f"{location}/{country} {location_time} Weather: "
            f"{temperature} Celsius, {condition_text}"
        )
    else:
        logging.warning("Failed to retrieve weather information.")


def get_weather(api_key: str) -> None:
    logging.info(
        f"Performing request to Weather API for city {DEFAULT_CITY}..."
    )
    data = fetch_weather_data(api_key, DEFAULT_CITY)
    display_weather_info(data)


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if api_key:
        get_weather(api_key)
    else:
        logging.error(
            "API_KEY not found. Please set the environment variable."
        )
