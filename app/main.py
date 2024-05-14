import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"


def get_weather() -> None:
    res = requests.get(URL)

    if res.status_code != 200:
        print("Something went wrong!")
        return None

    data = res.json()
    weather_description = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    print(f"The weather in Paris is {weather_description} "
          f"with a temperature of {temperature}°C.")


if __name__ == "__main__":
    get_weather()
