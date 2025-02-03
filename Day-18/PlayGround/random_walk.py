import turtle as t
from random import random, choice, randint
from turtle import Turtle

tim = t .Turtle()
t.colormode(255)

def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_colour = (r, g, b)
    return random_colour

random_num = [0 , 90 , 180 , 360]

for _ in range (200):
    tim.color(random_colour())
    tim.pensize(20)
    tim.speed(10.5)
    tim.forward(30)
    tim.setheading(choice(random_num))