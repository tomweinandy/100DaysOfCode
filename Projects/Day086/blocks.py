from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (1000, 1000)


class Block(Turtle):
    """
    Block class that inherits the Turtle class
    """
    def __init__(self, x=0, y=0, color='purple'):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2.6)
        self.color(color)
        self.goto(x, y)
        self.points_dict = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}   # define points earned by block color

    def popped_points(self):
        """
        Banishes a block
        :return: The point value of the popped block
        """
        self.goto(ISLAND_OF_MISFIT_TOYS)
        return self.points_dict[self.color()[0]]


class Row(Turtle):
    """
    Row class that inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.blocks = []

    def build(self, x, y, width, spacing, color):
        """
        Builds a horizontal row of block objects
        :param x: X coordinate of the first block in the row
        :param y: Y coordinate of the first block in the row
        :param width: The number of blocks that make up a row
        :param spacing: The space between each block
        :param color: Block color
        """
        for n in range(width):
            x_new = x + (n - 1) * spacing
            block = Block(x_new, y, color)
            self.blocks.append(block)

        # Clears away the turtle
        self.penup()
        self.goto(ISLAND_OF_MISFIT_TOYS)
