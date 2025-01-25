import requests


API_KEY = "c2a2981bc3344945b2c144432252301"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather():
    print("Performing request to Weather api for Paris...")
    url = f"{BASE_URL}?key={API_KEY}&q=Paris"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            city = data["location"]["name"]
            country = data["location"]["country"]
            localtime = data["location"]["localtime"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            print(f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")
        else:
            print(f"Error: Unable to fetch weather data (status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    get_weather()
