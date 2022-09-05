from turtle import Turtle
import laser
import random

ISLAND_OF_MISFIT_TOYS = (1000, 1000)
LASER_COUNT = 10


class Mothership(Turtle):
    """
    Invader class that inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.right(90)
        self.lasers = []
        self.create_lasers()
        self.moving_left = True
        self.goto(500, 300)

    def create_lasers(self):
        for i in range(LASER_COUNT):
            new_laser = laser.Laser('invader', ISLAND_OF_MISFIT_TOYS)
            self.lasers.append(new_laser)

    def fire_laser(self, invaders_hit):
        """
        Fires a laser beam at the defender. "We're gonna need a bigger spaceship."
        """
        self.laser.goto(self.position())

    def hit(self):
        """
        Banishes an invader
        """
        self.goto(ISLAND_OF_MISFIT_TOYS)

    def move(self):
        # Move left
        if self.moving_left:
            new_x = self.xcor() - 4
            self.goto(new_x, self.ycor())

            # In 1/40 times, start moving right
            if random.randint(1, 40) == 1:
                self.moving_left = False

        if not self.moving_left:
            # Move right
            new_x = self.xcor() + 4
            self.goto(new_x, self.ycor())

            # In 1/20 times, start moving left
            if random.randint(1, 20) == 1:
                self.moving_left = True
