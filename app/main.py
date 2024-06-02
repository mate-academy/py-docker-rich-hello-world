import os
import requests

API_KEY = os.environ.get("API_KEY")
FILTERING = "Paris"
URL = "https://api.weatherapi.com/v1"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError(
            "No API key provided.Set the WEATHER_API_KEY environment variable."
        )

    url = f"{URL}/current.json?key={API_KEY}&q={FILTERING}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Current temperature in", FILTERING, ":",
              data["current"]["temp_c"], "°C")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()