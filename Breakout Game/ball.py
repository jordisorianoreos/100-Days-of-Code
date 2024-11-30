from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 2
        self.move_speed = 0.05
        self.max_x_speed = 3  # Maximum speed in x
        self.max_y_speed = 2  # Maximum speed in y

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # Limit the speed in y to the maximum speed
        if abs(self.y_move) > self.max_y_speed:
            self.y_move = self.max_y_speed if self.y_move > 0 else -self.max_y_speed

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        # Limit the speed in x to the maximum speed
        if abs(self.x_move) > self.max_x_speed:
            self.x_move = self.max_x_speed if self.x_move > 0 else -self.max_x_speed
        # Move the ball slightly inward to avoid getting stuck
        self.setx(self.xcor() + self.x_move)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_y()