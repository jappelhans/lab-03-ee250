import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "6504cd64f13bad0c6899c6f66a33a4c9"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

def KtoF(K):
    F = 1.8*(K-273)+32
    F = round(F,1)
    return F


# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def main():
    city = "Las Vegas"
    temp = get_weather(city)
    # print(temp)

    data = temp["main"]

    print("City: ", temp["name"], sep="")
    print("Current temp: ", KtoF(data["temp"]), " ", chr(176), "F", sep="")
    print("Feels like:   ", KtoF(data["feels_like"]), " ", chr(176), "F", sep="")
    print("High today:   ", KtoF(data["temp_max"]), " ", chr(176), "F", sep="")
    print("Low today:    ", KtoF(data["temp_min"]), " ", chr(176), "F", sep="")
    print("Humidity:     ", data["humidity"], "%", sep="")


if __name__ == "__main__":
    main()
