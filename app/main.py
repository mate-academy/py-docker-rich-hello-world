import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        return "Failed to get api key"
    city_name = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        country_name = data["location"]["country"]
        timing = data["location"]["localtime"]
        condition = data["current"]["condition"]["text"]
        print(f"{city_name}/{country_name} {timing} "
              f"Weather {temperature} Celsius {condition}")
        return response.json()


if __name__ == "__main__":
    get_weather()
