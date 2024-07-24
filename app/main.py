import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(
            f"Weather in {CITY}: {data["current"]["condition"]["text"]}, "
            f"{data["current"]["temp_c"]}°C"
        )
    else:
        print("Error fetching weather data:", response.status_code)


if __name__ == "__main__":
    get_weather()
