from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()  # Display initial scores

    def update_scoreboard(self):
        """Clear and update the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase left player’s score and update the scoreboard"""
        self.l_score += 1
        self.update_scoreboard()
        if self.l_score == 10:
            self.game_over("Left Player Wins!")

    def r_point(self):
        """Increase right player’s score and update the scoreboard"""
        self.r_score += 1
        self.update_scoreboard()
        if self.r_score == 10:
            self.game_over("Right Player Wins!")

    def game_over(self, winner):
        """Display the game over message"""
        self.goto(0, 0)
        self.write(winner, align="center", font=("Courier", 30, "bold"))
