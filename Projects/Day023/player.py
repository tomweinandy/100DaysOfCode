from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """
        Super class inherited from the Turtle classes used to track the player information and function
        """
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        """
        Moves the player up (turtles never look back)
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset_position(self):
        """
        Returns the player to the starting position
        """
        self.goto(STARTING_POSITION)
