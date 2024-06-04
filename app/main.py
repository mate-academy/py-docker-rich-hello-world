import requests
from datetime import datetime


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    current_time = datetime.now()
    api_key = "fd7527de292449a3bd2104214240306"
    city = "Paris"
    current_date_str = current_time.strftime("%Y-%m-%dT%H:%M")
    response = requests.get(url, params={"key": api_key, "q": city})
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
