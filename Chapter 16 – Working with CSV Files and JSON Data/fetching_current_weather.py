#!python
#https://openweathermap.org/api/

import json, sys, requests

if len(sys.argv) > 2:
    city = ','.join(sys.argv[1:])

    appid = input('Please enter your App ID: ')

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city, appid)

    res = requests.get(url)
    res.raise_for_status()

    jsonData = json.loads(res.text)

    city = jsonData['name']
    weather = jsonData['weather'][0]['description']
    temp = round(jsonData['main']['temp'] - 272.15,2)

    print("The weather in {} is {} and temperature is {} degrees C".format(city, weather, temp))