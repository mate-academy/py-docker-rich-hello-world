import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


def get_weather(city: str, api_key: str) -> None:
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    location = weather_data["location"]
    current = weather_data["current"]

    city_name = location["name"]
    country = location["country"]
    localtime = location["localtime"]

    date_time_obj = datetime.strptime(localtime, "%Y-%m-%d %H:%M")
    year = date_time_obj.year
    month = date_time_obj.month
    day = date_time_obj.day
    hour = date_time_obj.hour
    minute = date_time_obj.minute

    temperature = current["temp_c"]
    updated_at = current["last_updated"]
    condition = current["condition"]["text"]

    print(f"City: {city_name}, Country: {country}")
    print(f"Date: {year}-{month:02}-{day:02} {hour:02}:{minute:02}")
    print(f"Weather: {temperature}°C, {condition}, updated_at: {updated_at}")


if __name__ == "__main__":
    get_weather("Paris", api_key=os.getenv("WEATHER_API_KEY"))
