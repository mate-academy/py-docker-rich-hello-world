import os
import requests
import time


BASE_URL = "http://api.weatherapi.com/v1/current.json"
Q_FILTER = "Paris"


def get_weather() -> None:
    url = (
        f"{BASE_URL}?key={os.getenv('API_KEY')}&q={Q_FILTER}"
    )
    print("Perfoming request to WeatherAPI for city Paris...")
    result = requests.get(url).json()
    for _ in range(3):
        time.sleep(0.5)
        print("........................")
    condition = result["current"]["condition"]["text"]
    local_time = result["location"]["localtime"]
    weather = f"Weather: {result['current']['temp_c']} Celsius, {condition}"

    print(f"Paris/France, {local_time}, {weather}")


if __name__ == "__main__":
    get_weather()
