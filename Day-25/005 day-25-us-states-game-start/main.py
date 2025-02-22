import turtle as t
from mimetypes import guess_type
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

states = pandas.read_csv('50_states.csv')
state_lists = states.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Corrected", prompt="What's another state name?")
    if answer_state and any(state.casefold() == answer_state.casefold() for state in state_lists):  # Case-insensitive check
        guessed_state.append(answer_state)
        state_data = states[states.state == answer_state]
        marker = Turtle()  # Use a new name instead of `t`
        marker.hideturtle()
        marker.penup()
        marker.goto(int(state_data.x), int(state_data.y))
        marker.write(answer_state, align="center", font=("Arial", 10, "normal"))

    else:
        screen.textinput(title="Incorrect!", prompt="Try again. Enter a valid state name:")

screen.exitonclick()
