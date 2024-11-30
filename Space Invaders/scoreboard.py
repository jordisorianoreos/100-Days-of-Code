from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Level: {self.level}  |  Score: {self.score}", align="center", font=("Terminal", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Terminal", 36, "normal"))
        time.sleep(2)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()
