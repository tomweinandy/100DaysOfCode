from turtle import Turtle

# Define constants
CEILING_YCOR = 330
FLOOR_YCOR = -330
ISLAND_OF_MISFIT_TOYS = (-1000, 1000)
LASER_SPEED = 7


class Laser(Turtle):
    """
    Laser class that inherits Turtle class. To quote Lupe Fiasco: 'lay.. zer'.
    """
    def __init__(self, invader_or_defender_type, position):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_len=0.1, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.type = invader_or_defender_type

        if self.type == 'invader':
            self.color('white')
        elif self.type == 'defender':
            self.color('green')
        elif self.type == 'mothership':
            self.color('yellow')

    def move(self):
        """
        Moves lasers from the invaders and mothership down, moves lasers from the defender up
        """
        if self.type == 'invader' or self.type == 'mothership':
            new_y = self.ycor() - LASER_SPEED
        elif self.type == 'defender':
            new_y = self.ycor() + LASER_SPEED
        self.goto(self.xcor(), new_y)
