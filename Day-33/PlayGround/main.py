import requests
#http://api.open-notify.org/iss-now.json
result = requests.get(url='http://api.open-notify.org/iss-now.json')
result.raise_for_status()

longitude_data = result.json()['iss_position']['longitude']
latitude_data = result.json()['iss_position']['latitude']

iss_position = (longitude_data , latitude_data)
print (iss_position)