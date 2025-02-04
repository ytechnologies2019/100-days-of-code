import turtle as t
from turtle import Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your colour: ")

is_race_on = False

colours = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
turtles = []
y_positions = [-100, -60, -20, 20, 60, 100]  # Adjusted positions for turtles

# Create turtles
for i in range(len(colours)):
    new_turtle = t.Turtle(shape="turtle")  # Create a new Turtle object
    new_turtle.color(colours[i])  # Set the turtle's color
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])  # Move to starting position
    turtles.append(new_turtle)  # Append to the turtles list

# Start the race if the user placed a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)  # Move each turtle forward

        # Check if a turtle reaches the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost. The {winning_color} turtle won the race.")
            break  # Stop the race

screen.exitonclick()
