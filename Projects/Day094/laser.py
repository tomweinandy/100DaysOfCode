from turtle import Turtle
import time

CEILING_YCOR = 330
FLOOR_YCOR = -330
ISLAND_OF_MISFIT_TOYS = (1000, 1000)


class Laser(Turtle):
    """
    Laser class that inherits Turtle class
    """
    def __init__(self, invader_or_defender_type, position):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_len=0.1, stretch_wid=1)
        self.penup()
        self.goto(position)
        # self.goto(ISLAND_OF_MISFIT_TOYS)
        self.speed = 1                              # starting speed of the laser
        self.type = invader_or_defender_type

        if self.type == 'invader':
            self.color('white')

        elif self.type == 'defender':
            self.color('green')

    def move(self):
        if self.type == 'invader':
            # while self.ycor() > FLOOR_YCOR:
            if True:
                new_y = self.ycor() + 3
                self.goto(self.xcor(), new_y)

        elif self.type == 'defender':
            # while self.ycor() < CEILING_YCOR:
            if True:
                new_y = self.ycor() + 3
                self.goto(self.xcor(), new_y)

        # self.goto(ISLAND_OF_MISFIT_TOYS)

