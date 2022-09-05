from turtle import Turtle
import laser
import random

ISLAND_OF_MISFIT_TOYS = (-1000, 1000)
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
        self.color('yellow')
        self.right(90)
        self.lasers = []
        self.create_lasers()
        self.position_of_last_laser_used = 0
        self.moving_left = True
        self.goto(500, 300)

    def create_lasers(self):
        """
        Creates a list of lasers and "stores" them on the island of misfit toys
        """
        for i in range(LASER_COUNT):
            new_laser = laser.Laser('mothership', ISLAND_OF_MISFIT_TOYS)
            self.lasers.append(new_laser)

    def fire_laser(self):
        """
        Fires a laser beam at the defender. "We're gonna need a bigger spaceship."
        """
        # Go to next laser in list (modulo makes 1 after the total count return to 0)
        position_of_next_laser = (self.position_of_last_laser_used + 1) % LASER_COUNT
        self.position_of_last_laser_used = position_of_next_laser

        # Fire the laser
        self.lasers[position_of_next_laser].goto(self.position())

    def hit(self):
        """
        Banishes the mothership
        """
        self.goto(ISLAND_OF_MISFIT_TOYS)

    def move(self):
        """
        Moves the mothership, mostly left, but randomly will change direction to psych out opponent. I bet you didn't
        know a turtle could do that. Well, the mother turtle can!
        """
        # Move left
        if self.moving_left:
            new_x = self.xcor() - 4
            self.goto(new_x, self.ycor())

            # In 1/40 of the times, start moving right
            if random.randint(1, 40) == 1:
                self.moving_left = False

        # Move right
        if not self.moving_left:
            new_x = self.xcor() + 4
            self.goto(new_x, self.ycor())

            # In 1/20 of the times, start moving left
            if random.randint(1, 20) == 1:
                self.moving_left = True
