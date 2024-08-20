import os

import requests

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    city = input("Enter city name: ")
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data.get('location').get('name')}")
        print(f"Country: {data.get('location').get('country')}")
        print(f"Timezone: {data.get('location').get('tz_id')}")
        print(f"Weather: {data.get('current').get('condition').get('text')}")
        print(f"Temperature: {data.get('current').get('temp_c')}")
        print(f"Feels like: {data['current']['feelslike_c']}")
    else:
        print("Please, enter valid location")


if __name__ == "__main__":
    get_weather()
