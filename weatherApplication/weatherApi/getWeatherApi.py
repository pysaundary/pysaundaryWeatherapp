import json
import time
import urllib.request
from rest_framework.status import HTTP_404_NOT_FOUND
api_key = "ab97b407c69ae7346f544843100d085b"
# city_name = input("Enter City Name : " )
# days=input('please enter the days between 1 to 16 : ')
base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

def get_weather(api, location_id):
    url = base_url + location_id +'&APPID='+api
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)
    return data


timestamp = time.time()
# get_weather(api_key,city_name)
