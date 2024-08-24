import requests
import os


API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

URL = "http://api.weatherapi.com/v1/current.json"

CITY = "Paris"


def get_weather() -> None:

    params = {
        "key": API_KEY,
        "q": CITY
    }

    title_request = f"Performing request to Weather API for city {CITY}..."

    result = requests.get(URL, params=params)

    if result.status_code == 200:
        data_paris = result.json()
        location = (f"{data_paris['location']['name']}/"
                    f"{data_paris['location']['country']}")
        local_time = f"{data_paris['location']['localtime']}"
        weather = (f" Weather: {data_paris['current']['temp_c']} "
                   f"Celsius, {data_paris['current']['condition']['text']}")
        print(f"{title_request} \n{location} {local_time} {weather}")
    else:
        print(f"Failed to retrieve data: {result.status_code}\n"
              f"Response: {result.text}")


if __name__ == "__main__":
    get_weather()
