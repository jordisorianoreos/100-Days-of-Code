import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import pygame

# Sounds
pygame.init()
pygame.mixer.init()
brick_sound = pygame.mixer.Sound("sounds/brick.mp3")
paddle_sound = pygame.mixer.Sound("sounds/paddle.mp3")
nextlevel_sound = pygame.mixer.Sound("sounds/nextlevel.mp3")
gameover_sound = pygame.mixer.Sound("sounds/gameover.mp3")
wall_sound = pygame.mixer.Sound("sounds/wall.mp3")

# Screen Config
sc_width = 800
sc_height = 600
level_scores = list(range(50, 10001, 50))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=sc_width, height=sc_height)
screen.title("Breakout")
screen.tracer(0)

# Initialize Objects
paddle = Paddle((0, -sc_height / 2 + 50))
ball = Ball()
scoreboard = Scoreboard()

def create_bricks():
    bricks = []
    brick_rows = 5
    brick_cols = 10
    brick_width = 80
    brick_height = 20
    x_start = -sc_width / 2 + brick_width / 2
    y_start = sc_height / 2 - brick_height - 40

    colors = ["red", "darkorange", "gold", "green", "mediumblue", "indigo"]

    for row in range(brick_rows):
        brick_color = colors[row]
        for col in range(brick_cols):
            brick_x = x_start + col * brick_width
            brick_y = y_start - row * brick_height
            brick = Brick((brick_x, brick_y), brick_color)
            bricks.append(brick)
    return bricks

def clear_bricks():
    for brick in bricks:
        brick.goto(1000, 1000)
    bricks.clear()

def move_paddle_with_mouse(event):
    x = event.x - sc_width / 2
    if -sc_width / 2 + 20 < x < sc_width / 2 - 20:
        paddle.goto(x, paddle.ycor())

# Assign mouse movement to the function using the Motion event
screen.cv.bind("<Motion>", move_paddle_with_mouse)
screen.cv.focus_force()

# Create initial bricks
bricks = create_bricks()

# Level control variable
next_level_triggered = False


# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with walls (top and bottom)
    if ball.ycor() > sc_height / 2 - 10:
        ball.bounce_y()
        wall_sound.play()

    if ball.xcor() > sc_width / 2 - 10 or ball.xcor() < -sc_width / 2 + 10:
        ball.bounce_x()
        wall_sound.play()

    # Detect collision with the paddle
    if ball.distance(paddle) < 58 and ball.ycor() < -sc_height / 2 + 60 and ball.y_move < 0:
        paddle_sound.play()
        diff = ball.xcor() - paddle.xcor()
        ball.bounce_y()
        ball.x_move += diff * 0.05

    # Detect collision with the bricks
    for brick in bricks[:]:
        if ball.distance(brick) < 45:
            ball.bounce_y()
            brick.goto(1000, 1000)
            brick_sound.play()
            bricks.remove(brick)
            scoreboard.increase_score()

    # Detect if the ball falls below the paddle (loss)
    if ball.ycor() < -sc_height / 2 + 5:
        gameover_sound.play()
        scoreboard.game_over()
        game_is_on = False

    # Detect if 50 points have been reached and activate the next level
    if scoreboard.score in level_scores:
        clear_bricks()
        nextlevel_sound.play()
        ball.goto(0, 0)
        bricks = create_bricks()
        level_scores.pop(0)
        scoreboard.next_level()
        ball.x_move *= 1.5
        ball.y_move *= 1.5
        ball.max_x_speed += 1.5
        ball.max_y_speed += 1.5
        time.sleep(2)

screen.exitonclick()