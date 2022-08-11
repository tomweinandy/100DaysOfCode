from turtle import Turtle


class Paddle(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.turtlesize(stretch_len=8, stretch_wid=0.5)
        self.penup()
        self.goto(x, y)
        self.keys_pressed = {}

    def move_right(self):
        """
        Action to move a paddle right 20 units (one square)
        """
        if self.xcor() < 410:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def move_left(self):
        """
        Action to move a paddle left 20 units (one square)
        """
        if self.xcor() > -410:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
