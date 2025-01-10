import requests

URL = "https://api.weatherapi.com/v1/"
API_KEY = "171e9f9e10f54ee4a5a144342250901"
FILTERING = "London"


def get_weather() -> None:
    response = requests.get(f"{URL}current.json?key={API_KEY}&q={FILTERING}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
