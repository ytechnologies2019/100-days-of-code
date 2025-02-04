import turtle as t
tim = t.Turtle()
import random

num_sides = 10

colours = ["red" , "green" , "DeepSkyBlue" , "LightSeaGreen" , "wheat"]

def draw_shape(num_sides):
    num = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(num)

for shade_side in range (3, 12):
    tim.color(random.choice(colours))
    draw_shape(shade_side)


