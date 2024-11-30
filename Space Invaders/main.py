import time
from turtle import Screen
from spaceship import Spaceship
from bullet_spaceship import BulletSp
from bullet_alien import BulletAl
from obstacles import Obstacle
from scoreboard import Scoreboard
from alien import Alien
import pygame
import random

# Sounds
pygame.init()
pygame.mixer.init()
nextlevel_sound = pygame.mixer.Sound("sounds/nextlevel.mp3")
gameover_sound = pygame.mixer.Sound("sounds/gameover.mp3")
explosion_sound = pygame.mixer.Sound("sounds/explode.mp3")
shot_sound = pygame.mixer.Sound("sounds/shot.mp3")

# Screen configuration
sc_width, sc_height = 800, 700
alien_rows, alien_cols = 5, 10
speed_increment, shoot_probability = 1, 0.0005
last_shot_time, cooldown = 0, 1
level_scores = [i * (alien_rows * alien_cols) for i in range(1, 11)]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=sc_width, height=sc_height)
screen.title("Space Invaders")
screen.tracer(0)

# Initialize objects
spaceship = Spaceship((0, -sc_height / 2 + 50))
obstacles = [Obstacle(pos) for pos in [(-350, -100), (-50, -100), (250, -100)]]
scoreboard = Scoreboard()
bullets_sp, bullets_al = [], []


def create_aliens():
    aliens, alien_width, alien_height = [], 50, 30
    x_start, y_start = 0 - alien_width * alien_cols / 2, sc_height / 2 - alien_height
    colors = ["#004d00", "#1A5319", "#508D4E", "#80AF81", "#D6EFD8"]
    for row in range(alien_rows):
        for col in range(alien_cols):
            alien_x, alien_y = x_start + col * alien_width, y_start - row * alien_height - 40
            aliens.append(Alien((alien_x, alien_y), colors[row]))
    return aliens


def clear_screen():
    for entity in aliens + bullets_sp + bullets_al:
        entity.goto(1000, 1000)
    aliens.clear(), bullets_sp.clear(), bullets_al.clear()
    for obstacle in obstacles:
        for block in obstacle.blocks:
            block.goto(1000, 1000)
    obstacles.clear()


def move_paddle_with_mouse(event):
    x = event.x - sc_width / 2
    if -sc_width / 2 + 20 < x < sc_width / 2 - 20:
        spaceship.goto(x, spaceship.ycor())


def shoot_bullet():
    global last_shot_time
    if time.time() - last_shot_time >= cooldown:
        bullet_sp = BulletSp()
        bullet_sp.goto(spaceship.xcor(), spaceship.ycor() + 20)
        bullets_sp.append(bullet_sp)
        last_shot_time = time.time()
        shot_sound.play()


def random_probability():
    return random.random() < shoot_probability


def move_aliens():
    global aliens_direction
    edge_reached = False
    for alien in aliens:
        alien.goto(alien.xcor() + aliens_direction * speed_increment, alien.ycor())
        if alien.xcor() > sc_width / 2 - 30 or alien.xcor() < -sc_width / 2 + 30:
            edge_reached = True
        if random_probability():
            shoot_alien_bullet(alien)
    if edge_reached:
        for alien in aliens:
            alien.goto(alien.xcor(), alien.ycor() - 8)
        aliens_direction *= -1


def shoot_alien_bullet(alien):
    bullet_al = BulletAl()
    bullet_al.color(alien.color()[0])
    bullet_al.setheading(270)
    bullet_al.goto(alien.xcor(), alien.ycor() - 20)
    bullets_al.append(bullet_al)


screen.cv.bind("<Motion>", move_paddle_with_mouse)
screen.cv.focus_force()
screen.onclick(lambda x, y: shoot_bullet())

aliens = create_aliens()
aliens_direction = 1
game_is_on = True

while game_is_on:
    screen.update()
    move_aliens()

    for bullet_sp in bullets_sp[:]:
        bullet_sp.move()
        if bullet_sp.ycor() > sc_height / 2 + 40:
            bullet_sp.disappear()

    for bullet_al in bullets_al[:]:
        bullet_al.move()
        if bullet_al.ycor() < -sc_height / 2 - 40:
            bullet_al.disappear()
        if bullet_al.distance(spaceship) < 15:
            gameover_sound.play()
            scoreboard.game_over()
            time.sleep(1)
            game_is_on = False

    for bullet_sp in bullets_sp[:]:
        for alien in aliens[:]:
            if bullet_sp.distance(alien) < 30:
                bullet_sp.disappear()
                alien.goto(1000, 1000)
                explosion_sound.play()
                aliens.remove(alien)
                scoreboard.increase_score()

    for alien in aliens:
        if alien.ycor() <= spaceship.ycor() + 15:
            gameover_sound.play()
            scoreboard.game_over()
            time.sleep(1)
            game_is_on = False

    for bullet_sp in bullets_sp[:]:
        for obstacle in obstacles:
            if obstacle.check_collision(bullet_sp):
                bullet_sp.disappear()

    for bullet_al in bullets_al[:]:
        for obstacle in obstacles:
            if obstacle.check_collision(bullet_al):
                bullet_al.disappear()

    if scoreboard.score in level_scores:
        clear_screen()
        obstacles = [Obstacle(pos) for pos in [(-350, -100), (-50, -100), (250, -100)]]
        speed_increment *= 1.6
        shoot_probability += 0.0007
        cooldown *= 0.92
        nextlevel_sound.play()
        aliens = create_aliens()
        level_scores.pop(0)
        scoreboard.next_level()

time.sleep(1)
screen.exitonclick()
