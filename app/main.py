import requests
import os


API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

FILTER = "Paris"


def get_weather() -> None:


    title_request = "Performing request to Weather API for city Paris..."
    result = requests.get(URL + FILTER)
    data_paris = result.json()
    location = (f"{data_paris['location']['name']}/"
                f"{data_paris['location']['country']}")
    local_time = f"{data_paris['location']['localtime']}"
    weather = (f" Weather: {data_paris['current']['temp_c']} "
               f"Celsius, {data_paris['current']['condition']['text']}")
    print(title_request)
    print(location + local_time + weather)


if __name__ == "__main__":
    get_weather()
