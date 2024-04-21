import requests


def get_weather() -> None:
    api_key = "5504e5df372a4f5794490902242104"
    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=" + city
    response = requests.get(url)
    data = response.json()
    location = data["location"]
    current = data["current"]
    print(f"Weather in {location["name"]}, {location["country"]}:")
    print(f"Temp: {current["temp_c"]} °C")
    print(f"Feels like: {current["feelslike_c"]} °C")
    print(f"Wind speed: {current["wind_kph"]} kp/h")
    print(f"Condition: {current["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
