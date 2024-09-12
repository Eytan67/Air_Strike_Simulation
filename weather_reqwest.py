from datetime import datetime, timedelta

import  requests
from urllib3 import request

from models.weather import Weather

key = 'dc822bb527b5e972c12fb7247808a6d9'


def get_location(city:str):
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}'

    respons = requests.get(url)
    data = respons.json()
    return {'lat':data[0]['lat'], 'lon':data[0]['lon']}



def get_weather_data(city:str):
    path = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}'

    request = requests.get(path)
    data = request.json()

    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    print(data['list'][0]['dt_txt'])
    data = list(filter(lambda x: (x['dt_txt']) == '2024-09-12 15:00:00', data['list'] ))[0]
    print(data)

    weather = Weather(data['weather'][0]['main'], data['clouds']['all'], data['wind']['speed'])
    # dict = {}
    # dict['weather'] = data['weather'][0]['main']
    # # print('weather', weather)
    # dict['clouds'] = data['clouds']['all']
    # # print('clouds', clouds)
    # dict['wind'] = data['wind']['speed']
    # print('wind', wind)
    return weather


    # city = data['city']
    # print(city)
    # lat = city['coord']['lat']
    # lon = city['coord']['lon']
    # print('lat', lat, 'lon', lon)

# get_weather_data(path)
