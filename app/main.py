import requests
import os

# from dotenv import load_dotenv
# load_dotenv('config.env')

api_key = os.getenv("WEATHER_API_KEY")


def get_weather() -> None:
    urls = "http://api.weatherapi.com/v1/current.json"
    params = {"q": "Paris", "lang": "uk", "key": f"{api_key}"}
    response = requests.get(urls, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
    # elif not api_key:

    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    get_weather()
