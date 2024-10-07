import os
import requests


def get_weather(api_key) -> None:
    # write your code here
    city = "Warsaw"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Temperature in the {city}: {temp_c}, weather: {condition}")



if __name__ == "__main__":
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("You have to pass API_KEY in the parameters")

    get_weather(api_key)
