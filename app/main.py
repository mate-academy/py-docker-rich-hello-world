import os

import requests


def get_weather(city: str = "Paris") -> None:
    print(f"Performing request to Weather API for city {city}...")
    url = (f"https://api.weatherapi.com/v1/current.json"
           f"?key={os.getenv('API_KEY')}&q={city}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
    else:
        response = response.json()
        city = response["location"]["name"]
        country = response["location"]["country"]
        local_time = response["location"]["localtime"]
        temperature = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]
        print(
            f"{city}/{country} {local_time} Weather: {temperature} Celsius, "
            f"{condition}"
        )


if __name__ == "__main__":
    get_weather()
