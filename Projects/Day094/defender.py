from turtle import Turtle
import laser

PADDLE_YCOR = -340
MOVING_DISTANCE = 8
LEFT_BARRIER = -455
RIGHT_BARRIER = 445
ISLAND_OF_MISFIT_TOYS = (1000, 1000)
LASER_RECHARGE = 75
LASER_COUNT = 5


class Defender(Turtle):
    """
    Build a Paddle class inherited from the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.blaster = None
        self.ship = None
        self.lasers = []
        self.position_of_last_laser_used = 0
        self.laser_recharge = 0
        self.create_defender()
        self.create_lasers()
        self.keys_pressed = {}  # allows for ship movement

    def create_defender(self):
        """
        Creates the defender object
        """
        # Make rectangle base of the defender
        new_ship = Turtle('square')
        new_ship.turtlesize(stretch_len=3, stretch_wid=1)
        new_ship.color('green')
        new_ship.penup()
        new_ship.goto(0, PADDLE_YCOR) #todo fix
        self.ship = new_ship

        # Add blaster to the defender
        new_blaster = Turtle()
        new_blaster.turtlesize(stretch_len=2, stretch_wid=2)
        new_blaster.color('green')
        new_blaster.penup()
        new_blaster.left(90)
        new_blaster.goto(0, PADDLE_YCOR + 25)
        self.blaster = new_blaster

    def create_lasers(self):
        for i in range(LASER_COUNT):
            new_laser = laser.Laser('defender', ISLAND_OF_MISFIT_TOYS)
            self.lasers.append(new_laser)

    def move_right(self):
        """
        Action to move the defender (base and blaster) to the right
        """
        # Only move defender is not past the RIGHT_BARRIER limit
        if self.ship.xcor() < RIGHT_BARRIER:
            self.ship.setx(self.ship.xcor() + MOVING_DISTANCE)
            self.blaster.setx(self.blaster.xcor() + MOVING_DISTANCE)

    def move_left(self):
        """
        Action to move the defender (base and blaster) to the left
        """
        # Only move defender is not past the LEFT_BARRIER limit
        if self.ship.xcor() > LEFT_BARRIER:
            self.ship.setx(self.ship.xcor() - MOVING_DISTANCE)
            self.blaster.setx(self.blaster.xcor() - MOVING_DISTANCE)

    def fire_laser(self):
        if self.laser_recharge <= 0:
            self.laser_recharge = LASER_RECHARGE
            # Go to next laser in list (modulo makes 1 after the total count return to 0)
            position_of_next_laser = (self.position_of_last_laser_used + 1) % LASER_COUNT
            self.position_of_last_laser_used = position_of_next_laser

            self.lasers[position_of_next_laser].goto(self.blaster.position())
            # print(position_of_next_laser, 'pew pew!')

    def change_color(self, color):
        self.ship.color(color)
        self.blaster.color(color)

    # def banish(self):
    #     """
    #     This is what we do to turtles that we do not want or like
    #     """
    #     self.ship.goto(ISLAND_OF_MISFIT_TOYS)
    #     self.blaster.goto(ISLAND_OF_MISFIT_TOYS)
