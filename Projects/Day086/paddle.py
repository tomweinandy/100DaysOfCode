from turtle import Turtle

PADDLE_YCOR = -340
PADDLE_CORS = [-80, -60, -40, -20, 0, 20, 40, 60, 80]
PADDLE_CORS_SHORT = [0, 20, 40, 60, 80]
MOVING_DISTANCE = 8
LEFT_BARRIER = -610
RIGHT_BARRIER = 600
SPINDEX = [40, 30, 20, 10, 0, -10, -20, -30, -40]
SPINDEX_SHORT = [30, 15, 0, -15, -30]
ISLAND_OF_MISFIT_TOYS = (1000, 1000)


class Paddle(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.segments = []
        self.paddle_cors = PADDLE_CORS
        self.paddle_cors_short = PADDLE_CORS_SHORT   # for when paddle is shortened
        self.last_x_cor = 0                          # tracks the last recorded location of the paddle
        self.create_paddle()
        self.spindex = SPINDEX                       # the paddle is "convex" and adds spin based on segment hit
        self.spindex_short = SPINDEX_SHORT           # for when paddle is shortened
        self.length = len(self.segments)
        self.keys_pressed = {}                       # allows for paddle movement

    def create_paddle(self):
        """
        Creates the paddle object
        """
        # Store each segment to a list within the paddle object
        self.segments = []
        for position in self.paddle_cors:
            new_turtle = Turtle('square')
            new_turtle.color('blue')
            new_turtle.penup()
            new_turtle.goto(self.last_x_cor + position, PADDLE_YCOR)
            self.segments.append(new_turtle)

            # Send the turtle off the display
            self.penup()
            self.goto(ISLAND_OF_MISFIT_TOYS)

    def move_right(self):
        """
        Action to move a paddle right
        """
        # Only move if the right-most segment is not past the RIGHT_BARRIER limit
        if self.segments[-1].xcor() < RIGHT_BARRIER:
            for seg in self.segments:
                seg.forward(MOVING_DISTANCE)

    def move_left(self):
        """
        Action to move a paddle left
        """
        # Only move if the left-most segment is not past the LEFT_BARRIER limit
        if self.segments[0].xcor() > LEFT_BARRIER:
            for seg in self.segments:
                seg.forward(-MOVING_DISTANCE)

    def banish(self):
        """
        This is what we do to turtles that we do not want or like
        """
        for seg in self.segments:
            seg.goto(ISLAND_OF_MISFIT_TOYS)
