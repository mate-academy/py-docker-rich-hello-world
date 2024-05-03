import os
import requests

CITY = "Paris"
API_KEY = os.environ.get("API_KEY")

def get_weather() -> None:
    res = requests.get(f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no")

    if res.status_code != 200:
        print("Something went")
        print(res.status_code)
        return
    if res.status_code == 200:
        data = res.json()
        data_location = data["location"]
        data_weather = data["current"]
        city = data_location["name"]
        country = data_location["country"]
        time = data_location["localtime"]
        temp = data_weather["temp_c"]
        weather_name = data_weather["condition"]["text"]
        print(f"Performing request to Weather API for city {city}...")
        print(
            f"{city}/{country} {time} "
            f"Weather : {temp} Celsius, {weather_name.capitalize()}"
        )



if __name__ == "__main__":
    get_weather()
