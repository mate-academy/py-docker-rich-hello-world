import requests
from datetime import datetime

API_KEY = "2a40a2a2837b4d50ae954326240506"
LOCATION = "Kharkiv"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        response = requests.get(URL, params={"key": API_KEY, "q": LOCATION})
        data = response.json()
        if response.status_code == 200:
            location_name = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            current_time = datetime.now().strftime("%y-%m-%d %H:%M")
            print(
                f"{location_name}/{country} {current_time}"
                f" Weather: {temp_c} Celsius, {condition}"
            )
        else:
            print(f"Failed to fetch weather data: {data['error']['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
