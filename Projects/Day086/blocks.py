from turtle import Turtle

ISLAND_OF_MISFIT_TOYS = (1000, 1000)


class Block(Turtle):
    def __init__(self, x=0, y=0, color='purple'):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2.7)
        self.color(color)
        self.goto(x, y)
        self.points_dict = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}

    def popped_points(self):
        self.goto(ISLAND_OF_MISFIT_TOYS)
        return self.points_dict[self.color()[0]]


class Row(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks = []

    def build(self, x, y, width, spacing, color):
        for n in range(width):
            x_new = x + (n - 1) * spacing
            block = Block(x_new, y, color)
            self.blocks.append(block)

        self.penup()
        self.goto(ISLAND_OF_MISFIT_TOYS)
