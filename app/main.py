import requests

FORMAT = "json"
API_KEY = "1fc28b99320e4fe19b393031243010"
URL = "https://api.weatherapi.com/v1/"
FILTERING = "Paris"


# https://api.weatherapi.com/v1/current.json?key=1fc28b99320e4fe19b393031243010&q=Paris
def get_weather() -> None:

    response = requests.get(
        URL + f"current.{FORMAT}?key={API_KEY}&q={FILTERING}"
    )
    print(response.status_code, response.json())


if __name__ == "__main__":
    get_weather()
