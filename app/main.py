import requests


def get_weather() -> None:
    api_key = "11ece046820c44a6877125738241708" #It's not safe to store the API key in code, but it's easier than in an environment variable :)
    url = "http://api.weatherapi.com/v1/current.json"
    key = api_key
    default_city = "Kyiv"

    try:
        params = {
            "q": default_city,
            "key": key,
            "aqi": "no"
        }
        response = requests.get(url, params=params)
    except:
        print("ERROR: API_KEY is not correct or invalid.")

    try:
        weather_data = response.json()
        print(f"Current weather in {weather_data['location']['name']}:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Weather: {weather_data['current']['condition']['text']}")
    except:
        print("ERROR: Connection failed.")


if __name__ == "__main__":
    get_weather()
