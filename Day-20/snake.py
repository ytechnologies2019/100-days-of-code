from turtle import Turtle

# Constants
starting_position = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of snake segments
move_distance = 20
up = 90
down = 270  # Corrected from 279
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial 3-segment snake."""
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        """Turns the snake upwards if it's not currently moving down."""
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        """Turns the snake downwards if it's not currently moving up."""
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        """Turns the snake left if it's not currently moving right."""
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        """Turns the snake right if it's not currently moving left."""
        if self.head.heading() != left:
            self.head.setheading(right)
