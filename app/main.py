import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    url = f"{URL}?key={API_KEY}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        current_time = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(f"{city}/{country} {current_time} "
              f"Weather: {temp} Celsius, {weather}")
    else:
        error_message = (
            response.json().get("error", {})
            .get("message", "Unknown error occurred")
        )
        print("Error:", error_message)


if __name__ == "__main__":
    get_weather()
