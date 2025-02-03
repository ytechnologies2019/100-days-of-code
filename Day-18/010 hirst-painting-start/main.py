import turtle as t
from random import randint

# Set up screen
screen = t.Screen()
screen.colormode(255)

# Create turtle
tummy = t.Turtle()
tummy.penup()
tummy.hideturtle()
tummy.speed("fastest")

# Function to generate a random color
def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# Move turtle to starting position
tummy.setheading(225)
tummy.forward(250)
tummy.setheading(0)

# Draw dots
number_of_dots = 101
for dot_count in range(1, number_of_dots):
    tummy.dot(20, random_colour())
    tummy.forward(50)

    if dot_count % 10 == 0:
        tummy.setheading(90)
        tummy.forward(50)
        tummy.setheading(180)
        tummy.forward(500)
        tummy.setheading(0)

screen.exitonclick()
