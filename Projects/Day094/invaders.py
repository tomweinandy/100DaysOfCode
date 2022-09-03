from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (1000, 1000)


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
        self.goto(x, y)
        # self.points_dict = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}   # define points earned by invader color

    def popped_points(self):
        """
        Banishes an invader
        :return: The point value of the popped invader
        """
        self.goto(ISLAND_OF_MISFIT_TOYS)
        # return self.points_dict[self.color()[0]]


class Row(Turtle):
    """
    Row class that inherits the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.invaders = []

    def build(self, x, y, width, spacing):
        """
        Builds a horizontal row of invaders objects
        :param x: X coordinate of the first invader in the row
        :param y: Y coordinate of the first invader in the row
        :param width: The number of invader that make up a row
        :param spacing: The space between each invader
        """
        for n in range(width):
            x_new = x + (n - 1) * spacing
            invader = Invader(x_new, y)
            invader.right(90)
            self.invaders.append(invader)

        # Clears away the turtle
        self.penup()
        self.goto(ISLAND_OF_MISFIT_TOYS)
