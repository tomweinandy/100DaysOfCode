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


class Defender(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """

    def __init__(self):
        super().__init__()
        self.my_ship = None
        self.paddle_cors = PADDLE_CORS
        self.paddle_cors_short = PADDLE_CORS_SHORT  # for when paddle is shortened
        self.last_x_cor = 0  # tracks the last recorded location of the paddle
        self.create_defender()
        self.spindex = SPINDEX  # the paddle is "convex" and adds spin based on segment hit
        self.spindex_short = SPINDEX_SHORT  # for when paddle is shortened
        # self.length = len(self.segments)
        self.keys_pressed = {}  # allows for paddle movement

    def create_defender(self):
        """
        Creates the defender object
        """
        # Make rectangle base of the defender
        new_ship = Turtle('square')
        new_ship.turtlesize(stretch_len=3, stretch_wid=1)
        new_ship.color('green')
        new_ship.penup()
        new_ship.goto(0, PADDLE_YCOR)
        self.my_ship = new_ship

        # Add blaster to the defender
        new_blaster = Turtle()
        new_blaster.turtlesize(stretch_len=2, stretch_wid=2)
        new_blaster.color('green')
        new_blaster.penup()
        new_blaster.left(90)
        new_blaster.goto(0, PADDLE_YCOR + 25)
        self.my_blaster = new_blaster

        # Send the turtle off the display
        # new_ship.goto(ISLAND_OF_MISFIT_TOYS)

        # # Store each segment to a list within the paddle object
        # self.segments = []
        # for position in self.paddle_cors:
        #     new_turtle = Turtle('square')
        #     new_turtle.color('blue')
        #     new_turtle.penup()
        #     new_turtle.goto(self.last_x_cor + position, PADDLE_YCOR)
        #     self.segments.append(new_turtle)
        #
        #     # Send the turtle off the display
        #     self.penup()
        #     self.goto(ISLAND_OF_MISFIT_TOYS)

    def move_right(self):
        """
        Action to move the defender (base and blaster) to the right
        """
        # Only move defender is not past the RIGHT_BARRIER limit
        if self.my_ship.xcor() < RIGHT_BARRIER:
            self.my_ship.setx(self.my_ship.xcor() + 10)
            self.my_blaster.setx(self.my_blaster.xcor() + 10)

    def move_left(self):
        """
        Action to move the defender (base and blaster) to the left
        """
        # Only move defender is not past the LEFT_BARRIER limit
        if self.my_ship.xcor() > LEFT_BARRIER:
            self.my_ship.setx(self.my_ship.xcor() - 10)
            self.my_blaster.setx(self.my_blaster.xcor() - 10)

    def fire_laser(self):
        print('pew pew!')

    def banish(self):
        """
        This is what we do to turtles that we do not want or like
        """
        self.my_ship.goto(ISLAND_OF_MISFIT_TOYS)
        self.my_blaster.goto(ISLAND_OF_MISFIT_TOYS)
