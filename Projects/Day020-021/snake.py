"""
Snake class
"""
import turtle

# Define constants
STARTING_POSITIONS = [(-250, 0), (-270, 0), (-290, 0)]
MOVING_DISTANCE = 20
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270


class Snake:
    """
    Creates a new class for the snake object
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates the snake object
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a segment to the snake
        :param position: the position of the last segment
        """
        new_turtle = turtle.Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        """
        Calls add_segment()
        """
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """
        Creates a new snake
        """
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """
        Make snake continuously move forward.
        Starting from the end of the snake, move each segment to position of previous segment.
        """
        # "-1" at the end reverses the order of the segments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def turn_up(self):
        """
        Prevents the snake from turning up if the snake's head is moving down
        """
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def turn_down(self):
        """
        Prevents the snake from turning down if the snake's head is moving up
        """
        if self.head.heading() != UP:
            self.head.setheading(270)

    def turn_left(self):
        """
        Prevents the snake from turning left if the snake's head is moving right
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def turn_right(self):
        """
        Prevents the snake from turning right if the snake's head is moving left
        """
        if self.head.heading() != LEFT:
            self.head.setheading(0)
