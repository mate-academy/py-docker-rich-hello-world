import requests
import os

API_KEY = os.getenv("API_KEY")
city = "Paris"

def get_weather() -> None:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Weather in {city}: {data['current']['temp_c']}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Unexpected response format.")

if __name__ == "__main__":
    get_weather()
