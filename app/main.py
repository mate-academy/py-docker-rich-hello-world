import requests
import os


WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather(api_key: str) -> None:
    with requests.get(
            WEATHER_API_URL,
            params={"key": api_key, "q": "London"}
    ) as request:
        if request.status_code != 200:
            print("Error: Can't get data from Weather API.")
            return

        request = request.json()
        print(
            f"{request['location']['name']}/{request['location']['country']} "
            f"{request['current']['last_updated']} "
            f"Weather: {request['current']['temp_c']} Celsius, "
            f"{request['current']['condition']['text']}"
        )


if __name__ == "__main__":
    get_weather(API_KEY)
