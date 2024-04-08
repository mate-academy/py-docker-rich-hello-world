import requests

API_KEY = "be47c9b11f124244959115558240804"


def get_weather() -> None:
    CITY = "Paris"
    URL = f"http://api.weatherapi.com/v1/current.json?"
    response = requests.get(f"{URL}key={API_KEY}&q={CITY}")
    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        wind_speed_km = data["current"]["wind_kph"]
        wind_speed_mile = data["current"]["wind_mph"]
        print(f"City: {CITY}\n"
              f"Temperature: {temp_c} °C ({temp_f} °F)\n"
              f"Wind Speed: {wind_speed_km} km ({wind_speed_mile} mile)")
        return
    print(f"Could not get weather, status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
