from itertools import count

country = input()
visits  = int(input())
lists_of_countries = eval((input()))

travel_log = [
    {
    "country" : "France" ,
    "visits" : 2 ,
    "cities" : ['Paris' , 'Lille' , 'Dijon' ]
},
{
    "country": "Germany",
    "visits": 2,
    "cities": ['Paris', 'Lille', 'Dijon']
},
]

# Allow new countries
def add_new_country(name, cities_visit, cities_name):
    new_country = {}
    new_country["country"] =  name
    new_country["visits"] =  cities_visit
    new_country["cities"] =  cities_name


##
# add_new_countries=(country,visit,lists_of_countries)
# print(f f"I've been travel to {travel_log}{'country'})
