import random
from turtle import Turtle

# todo rewrite this script as blocks, not cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class Block(Turtle):
    def __init__(self, x, y, color):
        """
        A car class inheriting the turtle class to create cars the form traffic
        """
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2.7)
        self.color(color)
        self.goto(x, y)


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
        self.blocks = []

    def build(self, x, y, width, spacing, color):
        for n in range(width):
            x_new = x + (n - 1) * spacing
            block = Block(x_new, y, color)
            # self.goto(x_new, self.y)
            # self.color()
            self.blocks.append(block)

        self.penup()
        self.goto(1000, 1000)


