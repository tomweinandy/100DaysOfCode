from turtle import Turtle
import time
import random


class Ball(Turtle):
    """
    Ball class that inherits Turtle class
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed = 1
        self.paused = True
        self.ceiling_hit = False
        self.orange_row_hit = False

        # Sets x and y direction as positive (i.e., is moving in northeast direction)
        self.x_direction = 1
        self.y_direction = 1

    def random_jitter(self):
        # if random.randint(0,1) == 1:
        #     self.right(10)
        # else:
        #     self.left(10)
        jitter = random.randint(-20, 20)
        self.right(jitter)

    def pause(self):
        """
        Pause ball movement (a little glitchy)
        """
        if self.paused:
            self.paused = False
        else:
            self.paused = True

    def move(self):
        """
        Sets ball in motion with direction defined by x_direction, y_direction
        """
        new_x = self.xcor() + 10*self.x_direction
        new_y = self.ycor() + 10*self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, x=False, y=False):
        """
        Flips the x or y direction depending on what it bounces off of
        :param x: True when bouncing off of the ceiling
        :param y: True when bouncing off of a paddle
        """
        if x:
            self.ceiling_hit = True
            self.x_direction *= -1
            self.random_jitter()
        if y:
            self.y_direction *= -1
            self.random_jitter()

    def increase_speed(self):
        """
        Increases speed by decreasing the pause between movements by 90%
        """
        self.speed *= 0.9

    def reset(self):
        """
        Resets the ball after a point is scored
        """
        time.sleep(1)
        self.speed = 1
        self.color('white')
        # Appears within a random point on the y-axis
        self.goto(0, random.randint(-250, 250))
        self.bounce(x=True, y=True)
