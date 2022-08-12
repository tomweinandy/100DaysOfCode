from turtle import Turtle

PADDLE_YCOR = -340
PADDLE_CORS = [(-250, PADDLE_YCOR), (-270, PADDLE_YCOR), (-290, PADDLE_YCOR)]
MOVING_DISTANCE = 20
LEFT_BARRIER = -410
RIGHT_BARRIER = 410


class Paddle(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """
    def __init__(self, x, y):
        super().__init__()
        # self.shape('square')
        # self.color('blue')
        # self.turtlesize(stretch_len=8, stretch_wid=0.5) #todo refactor paddle as list of connected segments
        # self.penup()
        # self.goto(x, y)
        self.segments = []
        self.create_paddle()
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
            new_turtle.goto(position)
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
