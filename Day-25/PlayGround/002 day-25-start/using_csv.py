# Old Method

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print (data)

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)

    temperature = []
    for row in data:
        if row[1] != "temp":      ## Remove the Temp Label
            temperature.append(row[1])
    print(temperature)