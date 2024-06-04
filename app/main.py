import requests
from decouple import config


API_KEY = config("API_KEY")
CITY_NAME = "Paris"
URL = (f"https://api.weatherapi.com/v1/current.json"
       f"?key={API_KEY}&q={CITY_NAME}&aqi=no")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY_NAME}...")
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data['location']['name']}/{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )
    elif response.status_code == 403:
        print("Some problem with your API_KEY!")

if __name__ == "__main__":
    get_weather()
