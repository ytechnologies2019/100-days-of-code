from datetime import datetime

import requests
import datetime as dt

username = 'thihathura'
TOKEN    = '12345678'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

users_params = {
    'token' : TOKEN,
    'username': username,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

response = requests.post(url=pixela_endpoint, json=users_params)
print("User Creation Response:", response.text)  # Print API response

# Graph Creation
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_config = {
    'id'   : GRAPH_ID,
    'name' : 'graph1',
    'unit' : 'Km',
    'type' : 'float',
    'color': 'ajisai',
}

xheaders = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=xheaders)
print("Graph Creation Response:", response.text)

# Adding Data to Graph
today = dt.datetime.now()
date_format = today.strftime('%Y%m%d')
pixela_creation_endpoint = f'{pixela_endpoint}/{username}/graphs/{GRAPH_ID}'
pixela_data = {
    'date': date_format ,
    'quantity': input("How many KM did you circle today? : "),
}

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=xheaders)
print("Graph Data Addition Response:", response.text)


want_to_update = input("Do you want to update your km ? : ")
if want_to_update == 'yes':
    update_endpoint = f'{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{date_format}'
    new_pixel_data = {
    }
    update = requests.put(url=update_endpoint , json=new_pixel_data , headers=xheaders)
    want_to_delete = input('Do you want to delete updated data? : ')

    if want_to_delete == 'yes':
        delete_endpoint = update_endpoint
        delete = requests.delete(url=delete_endpoint, headers=xheaders)
        print("Delete Data Response:", delete.text)
    else:
        print("Update Data Addition Response: ", update.text)

else:
    print ('There is no update data')
