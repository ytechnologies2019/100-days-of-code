from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard  # Import the Scoreboard class
import time

# Set up the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()  # Initialize scoreboard

# Listen for key presses
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Detect when the ball misses the paddles
    if ball.xcor() > 380:  # Right paddle misses
        ball.reset_position()
        scoreboard.l_point()  # Left player gets a point

    if ball.xcor() < -380:  # Left paddle misses
        ball.reset_position()
        scoreboard.r_point()  # Right player gets a point

screen.exitonclick()
