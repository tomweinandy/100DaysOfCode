from turtle import Turtle

PADDLE_YCOR = -340
PADDLE_CORS = [i for i in range(0, 160, 20)]
MOVING_DISTANCE = 7
LEFT_BARRIER = -610
RIGHT_BARRIER = 600


class Paddle(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """
    def __init__(self, x, y):
        super().__init__()
        self.segments = []
        self.create_paddle()
        self.length = len(self.segments)
        self.head = self.segments[0]
        self.keys_pressed = {}

    def create_paddle(self):
        """
        Creates the snake object
        """
        for position in PADDLE_CORS:
            new_turtle = Turtle('square')
            new_turtle.color('blue')
            new_turtle.penup()
            new_turtle.goto(position, PADDLE_YCOR)
            self.segments.append(new_turtle)

    def move_right(self):
        """
        Action to move a paddle right 20 units (one square)
        """
        # Only move if the right-most segment is not past the right wall
        if self.segments[-1].xcor() < RIGHT_BARRIER:
            for seg in self.segments:
                seg.forward(MOVING_DISTANCE)

    def move_left(self):
        """
        Action to move a paddle left 20 units (one square)
        """
        # Only move if the left-most segment is not past the left wall
        if self.segments[0].xcor() > LEFT_BARRIER:
            for seg in self.segments:
                seg.forward(-MOVING_DISTANCE)
