import requests
from decouple import config


API_KEY = config("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> None:
    print(f"Performing request to Weather API for city {city}...")
    response = requests.get(URL, params={"key": API_KEY, "q": city})

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
    get_weather(city="Paris")
