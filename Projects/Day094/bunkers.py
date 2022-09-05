from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (1000, 1000)
BUNKER_SHAPE = [[(i, 0) for i in range(0, 55, 5)],
                [(i, -5) for i in range(-5, 60, 5)],
                [(i, -10) for i in range(-10, 65, 5)],
                [(i, -15) for i in range(-15, 70, 5)],
                [(i, -20) for i in range(-15, 70, 5)],
                [(i, -25) for i in range(-15, 25, 5)] + [(i, -25) for i in range(30, 70, 5)],
                [(i, -30) for i in range(-15, 20, 5)] + [(i, -30) for i in range(35, 70, 5)],
                [(i, -35) for i in range(-15, 15, 5)] + [(i, -35) for i in range(40, 70, 5)],
                [(i, -40) for i in range(-15, 10, 5)] + [(i, -40) for i in range(45, 70, 5)],
                [(i, -45) for i in range(-15, 10, 5)] + [(i, -45) for i in range(45, 70, 5)],
                [(i, -50) for i in range(-15, 10, 5)] + [(i, -50) for i in range(45, 70, 5)],
                [(i, -55) for i in range(-15, 10, 5)] + [(i, -55) for i in range(45, 70, 5)]]


class Block(Turtle):
    """
    Block class that inherits the Turtle class
    """
    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=0.2, stretch_wid=0.2)
        self.color('green')
        self.goto(x, y)

    def hit(self):
        """
        Banishes a block
        :return: The point value of the popped block
        """
        self.goto(ISLAND_OF_MISFIT_TOYS)


class Bunker(Turtle):
    """
    Row class that inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.blocks = []

    def build(self, x, y):
        """
        Builds a horizontal row of block objects
        :param x: X coordinate of the first block in the row
        :param y: Y coordinate of the first block in the row
        :param width: The number of blocks that make up a row
        :param spacing: The space between each block
        """
        for row in BUNKER_SHAPE:
            for pair in row:
                block = Block(pair[0] + x, pair[1] + y)
                self.blocks.append(block)

        # Clears away the turtle
        # self.penup()
        # self.goto(ISLAND_OF_MISFIT_TOYS)
