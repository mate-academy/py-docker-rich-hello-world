import requests


def get_weather() -> str:
    response = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={"q": "Paris", "key": "8ba46685a31a4765b9455446242211"}
    )
    r_json = response.json()
    r_str = (
        f"{r_json["location"]["name"]}"
        f"/{r_json["location"]["country"]} "
        f"{r_json["location"]["localtime"]} "
        f"Weather: {r_json["current"]["temp_c"]} Celsius, "
        f"{r_json["current"]["condition"]["text"]}"
    )
    return r_str


if __name__ == "__main__":
    print(get_weather())
