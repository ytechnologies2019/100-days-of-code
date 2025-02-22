import pandas
from numpy.ma.core import maximum
from numpy.ma.extras import average
from pandas import Series

data = pandas.read_csv("weather_data.csv")

## 2 types of pandas
print(type(data))
print (type(data["temp"]))

data_dict = data.to_dict()
print (data_dict)

data_list = data["temp"].to_list()
print (data_list)

average_data = (int(sum(data_list)))
print (average_data)

maximum_data = data['temp'].max()
print(maximum_data)

print(data['condition'])

##Check the Data Days
check_day = data[data.day == "Monday"]
print(check_day)

