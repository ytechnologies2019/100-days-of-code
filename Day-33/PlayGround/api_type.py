import requests
import datetime as t

LAT = 50.123
LOG = -25.12
parameter = {
    'lat' : LAT,
    'lng' : LOG,
    'formatted' : 0 ,
}

url = 'https://api.sunrise-sunset.org/json'
response = requests.get(url, params=parameter)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise']
sunset  = data['results']['sunset']
print (sunrise.split('T') , sunset.split('T'))

time_now = t.datetime.now()
print (time_now)