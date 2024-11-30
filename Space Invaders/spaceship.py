from turtle import Turtle
from bullet_spaceship import BulletSp
import pygame

pygame.init()
pygame.mixer.init()
shot_sound = pygame.mixer.Sound("sounds/shot.mp3")


class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("classic")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=2)
        self.penup()
        self.goto(position)
        self.setheading(90)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 350 - 60:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -350 + 60:
            self.goto(new_x, self.ycor())

    def shoot_bullet(self):
        bullet = BulletSp()
        shot_sound.play()
        bullet.goto(self.xcor(), self.ycor())
        return bullet
