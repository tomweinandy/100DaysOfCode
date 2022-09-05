from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (-1000, 1000)
SPACING = 10
BLOCK_SIZE = 0.5
BUNKER_MOLD = [[(i, 0) for i in range(0, 55, SPACING)],
               [(i, -1*SPACING) for i in range(-5, 60, SPACING)],
               [(i, -2*SPACING) for i in range(-10, 65, SPACING)],
               [(i, -3*SPACING) for i in range(-15, 70, SPACING)],
               [(i, -4*SPACING) for i in range(-15, 20, SPACING)] + [(i, -4*SPACING) for i in range(35, 70, SPACING)],
               [(i, -5*SPACING) for i in range(-15, 15, SPACING)] + [(i, -5*SPACING) for i in range(45, 70, SPACING)],
               [(i, -6*SPACING) for i in range(-15, 10, SPACING)] + [(i, -6*SPACING) for i in range(45, 70, SPACING)],
               [(i, -7*SPACING) for i in range(-15, 10, SPACING)] + [(i, -7*SPACING) for i in range(45, 70, SPACING)]]


class Block(Turtle):
    """
    Block class that inherits the Turtle class
    """
    def __init__(self, x=0, y=0):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=BLOCK_SIZE, stretch_wid=BLOCK_SIZE)
        self.color('blue')
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
        Builds a barrier of bunkers
        :param x: X coordinate of the highest, left block
        :param y: Y coordinate of the highest, left block
        """
        for row in BUNKER_MOLD:
            for pair in row:
                block = Block(pair[0] + x, pair[1] + y)
                self.blocks.append(block)
