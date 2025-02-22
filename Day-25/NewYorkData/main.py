import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_color = len(data[data["Primary Fur Color"] == "Gray"])
red_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])

print(grey_color)
print(red_color)
print(black_color)

data_dict = {
    "Fur Colour": ['Gray' , 'Cinnamon' , 'Black' ] ,
    "Count" : [grey_color , red_color , black_color]
}

df = pandas.DataFrame(data_dict)
df_to_csv = df.to_csv("result.csv")