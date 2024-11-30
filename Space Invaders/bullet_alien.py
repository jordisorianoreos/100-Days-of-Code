from turtle import Turtle


class BulletAl(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.3, stretch_len=0.7)
        self.setheading(90)
        self.penup()
        self.x_move = 0
        self.y_move = 4
        self.active = True

    def move(self):
        if self.active:
            new_y = self.ycor() - self.y_move
            self.goto(self.xcor(), new_y)

    def disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)
        self.active = False


