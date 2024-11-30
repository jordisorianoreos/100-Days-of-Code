from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, brick_color):
        super().__init__()
        self.shape("square")
        self.color(brick_color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)
