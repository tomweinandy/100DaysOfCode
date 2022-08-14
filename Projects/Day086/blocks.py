import random
from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (1000, 1000)

# todo rewrite this script as blocks, not cars


class Block(Turtle):
    def __init__(self, x=0, y=0, color='purple'):
        """
        A car class inheriting the turtle class to create cars the form traffic
        """
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2.7)
        self.color(color)
        self.goto(x, y)
        self.points_dict = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}

    def popped_points(self):
        self.goto(1000, 1000)
        return self.points_dict[self.color()[0]]



class Row(Turtle):
    """
    A car class inheriting the turtle class to manage traffic patterns
    """
    def __init__(self):
        super().__init__()
        # self.starting_x = x
        # self.starting_y = y
        # self.width = width
        # self.color = color
        # self.spacing = spacing
        # self.first_orange_hit = False
        self.blocks = []

    def build(self, x, y, width, spacing, color):
        for n in range(width):
            x_new = x + (n - 1) * spacing
            block = Block(x_new, y, color)
            # self.goto(x_new, self.y)
            # self.color()
            self.blocks.append(block)

        self.penup()
        self.goto(ISLAND_OF_MISFIT_TOYS)

