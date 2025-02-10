import time
from turtle import Screen  # Importing required modules
from snake import Snake
from food import Food
from score_board import Scoreboard
# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Setting the screen size
screen.bgcolor('black')  # Background color of the screen
screen.title("My Snake Game")  # Title of the window
screen.tracer(0)  # Turns off automatic screen updates for smooth animation

snake = Snake()

food = Food()

score_board = Scoreboard()

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
    # Check for collision with food
    if snake.head.distance(food) < 15:  # If the snake eats the food
        food.refresh()  # Move food to a new random location
        snake.extend()
        score_board.increase_score()  # Correct function call
    ##Detect the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    ##Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()
