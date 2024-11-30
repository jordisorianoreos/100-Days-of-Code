from turtle import Turtle


class ObstacleBlock(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)


class Obstacle:
    def __init__(self, position):
        self.blocks = []
        self.create_obstacle(position)

    def create_obstacle(self, position):
        x_start, y_start = position
        for row in range(5):
            for col in range(6):
                block_x = x_start + col * 20
                block_y = y_start - row * 20
                block = ObstacleBlock((block_x, block_y))
                self.blocks.append(block)

    def check_collision(self, bullet):
        for block in self.blocks:
            if bullet.distance(block) < 15:
                block.goto(1000, 1000)
                self.blocks.remove(block)
                return True
        return False
