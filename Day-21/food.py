from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):  # Fixed constructor
        super().__init__()  # Fixed superclass constructor
        self.shape("circle")
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Corrected size
        self.refresh()  #  Place food in a random position

    def refresh(self):
        """Move the food to a new random location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
