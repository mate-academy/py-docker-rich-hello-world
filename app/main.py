import requests
import os

api_key = os.getenv("WEATHER_API_KEY")


def get_weather() -> None:
    urls = "http://api.weatherapi.com/v1/current.json"
    params = {"q": "Paris", "lang": "uk", "key": f"{api_key}"}
    response = requests.get(urls, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
    elif response.status_code == 404:
        print("Not Found")
    else:
        print(
            f"Error: Failed to retrieve weather data. "
            f"Status Code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
