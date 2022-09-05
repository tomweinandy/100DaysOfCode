from turtle import Turtle
import laser
import random

ISLAND_OF_MISFIT_TOYS = (-1000, 1000)
LASER_RECHARGE_INVADER = 280


class Invader(Turtle):
    """
    Invader class that inherits the Turtle class
    """
    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.turtlesize(stretch_len=0.8, stretch_wid=1.4)
        self.color('white')
        self.laser = laser.Laser('invader', ISLAND_OF_MISFIT_TOYS)
        # Assign random initial condition so lasers fire at different times
        self.laser_recharge = random.choice(range(LASER_RECHARGE_INVADER))
        self.alive = True
        self.moving_left = True
        self.starting_x = x
        self.goto(x, y)

    def fire_laser(self, invaders_hit):
        """
        Fires a laser beam at the defender. "It's turtles with friggin' lasers on their heads!"
        :param invaders_hit: Firing frequency increases with the number of invaders hit
        """
        if self.laser_recharge <= 0:
            # Add random adjustment to recharge time to keep things interesting
            # Add non-random adjustment to decrease recharge time as more invaders are hit
            adjustment = random.choice(range(-20, 20)) - 8*invaders_hit
            self.laser_recharge = LASER_RECHARGE_INVADER + adjustment
            self.laser.goto(self.position())

    def hit(self):
        """
        Banishes an invader
        """
        self.alive = False
        self.goto(ISLAND_OF_MISFIT_TOYS)

    def move(self):
        """
        Moves each invader back and forth across the screen and slowly down toward the defender.
        """
        # Move left (and a little down)
        if self.moving_left:
            new_x = self.xcor() - 4
            self.goto(new_x, self.ycor() - 0.1)
            if self.starting_x - self.xcor() >= 250:
                self.moving_left = False

        # Move right (and a little down)
        if not self.moving_left:
            new_x = self.xcor() + 4
            self.goto(new_x, self.ycor() - 0.1)
            if self.xcor() - self.starting_x >= 240:
                self.moving_left = True


class Column(Turtle):
    """
    Column class that inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.invaders = []

    def build(self, x, y, length, spacing):
        """
        Builds a vertical column of invader objects
        :param x: X coordinate of the first invader in the column
        :param y: Y coordinate of the first invader in the column
        :param length: The number of invader that make up a column
        :param spacing: The space between each invader
        """
        for n in range(length):
            y_new = y + (n + 1) * spacing
            invader = Invader(x, y_new)
            invader.right(90)
            self.invaders.append(invader)

            # Only keep the first invader in each column active
            if n > 0:
                invader.active = False

        # Clears away the turtle
        self.penup()
        self.goto(ISLAND_OF_MISFIT_TOYS)
