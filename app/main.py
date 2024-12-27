import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> str:
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY")
    if not api_key:
        raise ValueError("API_KEY is not set")
    if not city:
        raise ValueError("CITY is not set")

    url = "http://api.weatherapi.com/v1/current.json?"
    response = requests.get(url + f"key={api_key}&q={city}")
    if response.status_code == 200:
        return (
            f"{response.json()['location']['name']}/"
            f"{response.json()['location']['country']} "
            f"{response.json()['location']['localtime']} "
            f"Weather: {response.json()['current']['temp_c']} Celsius, "
            f"{response.json()['current']['condition']['text']}"
        )
    else:
        raise Exception(
            f"Error fetching weather data: "
            f" {response.status_code}, {response.text}"
        )


if __name__ == "__main__":

    try:
        weather = get_weather()
        print(weather)
    except Exception as e:
        print(f"Error: {e}")
