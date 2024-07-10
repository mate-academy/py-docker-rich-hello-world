from __future__ import print_function
import os
import swagger_client
import requests
from swagger_client.rest import ApiException
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
LANG = "en"
URL = "https://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    configuration = swagger_client.Configuration()
    configuration.api_key["key"] = API_KEY

    url = f"{URL}key={API_KEY}&q={CITY}&lang={LANG}"

    try:
        response = requests.get(url).json()
        print(f"{response['location']['country']}/"
              f"{response['location']['name']} "
              f"{response['location']['localtime']} "
              f"Weather: {response['current']['temp_c']} Celsius, "
              f"{response['current']['condition']['text']}")
    except ApiException as e:
        print(f"Exception when calling Weather API: {e}")


if __name__ == "__main__":
    get_weather()
