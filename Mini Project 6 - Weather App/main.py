import requests

def get_weather(city):
    api_key = "2a87b922565fd73f38d149fd93a00a53"
    base_url= "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()  # parsing the acutal data: response.text(JSON formatted string object) in to dict
        print(f"Weather in {city}: \n")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or error fetching data.", response.status_code)

city_name = input("Entr city name: ")
get_weather(city_name)
