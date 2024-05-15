import requests
from datetime import datetime


def get_weather() -> None:
    URL = "https://api.weatherapi.com/v1/current.json"
    city = "Paris"
    current_date = datetime.now()
    current_date_str = current_date.strftime("%Y-%m-%d %H:%M")
    api_key = "83df8e21cee84033bc8144312241305"

    response = requests.get(URL, params={"key": api_key, "q": city})
    weather_data = response.json()

    if "error" in weather_data:
        print("Error:", weather_data["error"]["message"])
    else:
        current_weather = weather_data["current"]
        print(f"Performing request to Weather API for city {city}...")
        print(
            f"{city}/France {current_date_str} Weather:",
            current_weather["temp_c"],
            "Celsius,",
            current_weather["condition"]["text"],
        )


if __name__ == "__main__":
    get_weather()
