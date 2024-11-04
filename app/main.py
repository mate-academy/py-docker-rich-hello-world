import requests
import os

from dotenv import load_dotenv

load_dotenv()
def get_weather() -> None:
    # write your code here
    URL = "http://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"
    API = os.getenv("API")

    response = requests.get(URL + f"key={API}&" + f"q={FILTERING}")
    print(response.json())

if __name__ == "__main__":
    get_weather()
