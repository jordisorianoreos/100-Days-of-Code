from turtle import Turtle


class BulletSp(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("classic")
        self.shapesize(stretch_wid=1, stretch_len=1.1)
        self.setheading(90)
        self.penup()
        self.x_move = 0
        self.y_move = 5
        self.active = True

    def move(self):
        if self.active:
            new_y = self.ycor() + self.y_move
            self.goto(self.xcor(), new_y)

    def disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)
        self.active = False


