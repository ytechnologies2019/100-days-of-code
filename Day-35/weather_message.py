import random

class Weather:
    def __init__(self):

        with  open("./so_hot.txt", "r") as sh:
            self.so_hot_line = sh.readlines()

        with open('./hot.txt') as h:
            self.hot_line = h.readlines()

        with open('./warm.txt') as w:
            self.warm_line = w.readlines()

        with open('./fine.txt') as f:
            self.fine_line = f.readlines()

    def so_hot(self):
        return random.choice(self.so_hot_line).strip()

    def hot_weather(self):
        return random.choice(self.hot_line).strip()

    def warm_weather(self):
        return random.choice(self.warm_line).strip()

    def find_weather(self):
        return random.choice(self.fine_line).strip()

weather = Weather()
so_hot_random_line = weather.so_hot()
hot_random_line    = weather.hot_weather()
warm_random_line   = weather.warm_weather()
find_random_line   = weather.find_weather()




