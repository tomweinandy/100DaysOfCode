import turtle
import random


class Food(turtle.Turtle):
    """
    A food class that inherits the properties of the turtle class
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('cyan')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
        Places a food pellet at a random location on the screen
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
