import os
import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def format_weather_data(data: dict) -> str:
    try:
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        formatted_result = (f"Location: {city_name}, {country}, |"
                            f"Time: {time}, |"
                            f"Temperature: {temperature}, |"
                            f"Condition: {condition}")

        return formatted_result
    except KeyError as e:
        return f"Error: Missing data in API response - {e}"


def get_weather() -> None:
    try:
        response = requests.get(f"{BASE_URL}key={API_KEY}&q={CITY}")
        response.raise_for_status()
        weather_data = response.json()
        print(format_weather_data(weather_data))
    except requests.exceptions.RequestException as error:
        print(f"Failed to get weather data: {error}")


if __name__ == "__main__":
    get_weather()
