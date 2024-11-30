from turtle import Turtle
from bullet_alien import BulletAl


class Alien(Turtle):

    def __init__(self, position, brick_color):
        super().__init__()
        self.shape("turtle")
        self.color(brick_color)
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(270)

    def shoot_bullet(self):
        bullet = BulletAl()
        bullet.goto(self.xcor(), self.ycor())
        return bullet
