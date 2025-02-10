import time
from turtle import Turtle, Screen  # Importing required modules
from snake import Snake

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Setting the screen size
screen.bgcolor('black')  # Background color of the screen
screen.title("My Snake Game")  # Title of the window
screen.tracer(0)  # Turns off automatic screen updates for smooth animation

snake = Snake()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True  # Flag to keep the game running
while game_is_on:
    screen.update()  # Refresh the screen with updated positions
    time.sleep(0.1)  # Adds delay for smooth movement
    snake.move()
# Close the window when clicked
screen.exitonclick()
