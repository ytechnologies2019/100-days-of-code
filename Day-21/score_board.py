from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):  # Fixed constructor
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)  # Move the scoreboard to the top
        self.update_scoreboard()  # Display initial score

    def update_scoreboard(self):
        """Updates the scoreboard display."""
        self.clear()  # Clears the previous score before updating
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0 , 0)
        self.write('GAME OVER' , align="center" , font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increases the score and updates the display."""
        self.score += 1
        self.update_scoreboard()  # Refresh score display
