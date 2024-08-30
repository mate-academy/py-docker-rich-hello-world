from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_request_url(city_name: str) -> str:
    base_url = "http://api.weatherapi.com/v1"
    current_weather_url = "/current.json"
    api_key = os.getenv("API_KEY")
    url = f"{base_url}{current_weather_url}?key={api_key}&q={city_name}"
    return url


def get_weather() -> None:
    url = get_request_url("Paris")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        location = data["location"]
        weather = data["current"]

        name, country, localtime = map(location.get,
                                       ["name", "country", "localtime"])
        temp_c = weather["temp_c"]
        condition = weather["condition"]["text"]

        data_string = (f"{name}/{country} {localtime} "
                       f"Weather: {temp_c} Celsius, {condition}")
        print(data_string)
    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == "__main__":
    get_weather()
