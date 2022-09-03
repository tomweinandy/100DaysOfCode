from turtle import Turtle
import time


class Ball(Turtle):
    """
    Ball class that inherits Turtle class
    """
    def __init__(self, ball_start_cors, ball_start_orientation):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(ball_start_cors)
        self.speed = 2                              # starting speed of the ball
        self.paddle_bounce_angle = 90               # ball will make 90 degree bounce (changes with spin)
        self.orientation = ball_start_orientation   # direction ball travels (polar coordinate degrees with 0=360=east)
        self.setheading(self.orientation)           # orients the ball
        self.paddle_hits = 0
        self.ceiling_hit = False
        self.orange_row_hit = False

    def bounce(self, wall, spin=0):
        """
        Causes the ball to "bounce" by changing orientation and the paddle bounce angle
        :param wall: Which wall it hits: 'top', 'bottom', 'left' or 'right'
        :param spin: Amount the ball spins based on part of paddle it hits (default is no spin)
        """
        if wall == 'left':
            # Change orientation based on if ball was travelling in the northwest or southwest direction
            if 90 < self.orientation <= 180:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 180 < self.orientation < 270:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360

        if wall == 'right':
            # Change orientation based on if ball was travelling in the southeast or northeast direction
            if 270 < self.orientation <= 360:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 0 <= self.orientation < 90:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360

        if wall == 'top':
            bounce_angle = 180 + self.paddle_bounce_angle

            # Change orientation based on if ball was travelling in the northeast or northwest direction
            if 0 < self.orientation <= 90:
                self.orientation = (self.orientation + bounce_angle) % 360
            elif 90 < self.orientation < 180:
                self.orientation = (self.orientation - bounce_angle) % 360

        if wall == 'bottom':
            # Change orientation based on spin and if ball was travelling in the southwest or southwest direction
            if 180 < self.orientation <= 270:
                bounce_angle = 180 + self.paddle_bounce_angle + spin
                self.orientation = (self.orientation + bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle + (2 * spin)

            if 270 < self.orientation < 360:
                bounce_angle = 180 + self.paddle_bounce_angle - spin
                self.orientation = (self.orientation - bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle - (2 * spin)

        # Force paddle bounce to be between 0 and 170 degrees
        if self.paddle_bounce_angle < 0:
            self.paddle_bounce_angle = abs(self.paddle_bounce_angle)
        if self.paddle_bounce_angle > 170:
            self.paddle_bounce_angle = 170

        # Set the new orientation
        self.setheading(self.orientation)
        # print(f'Wall: {wall}, Spin: {spin}, Paddle Bounce Angle: {self.paddle_bounce_angle},'
        #       f' Orientation: {self.orientation}')   # uncomment when debugging

    def speed_event(self, event):
        """
        Executes a speed event
        :param event: An event that increases the ball speed: 'four hits', 'twelve hits' or 'orange block'
        """
        if event == 'four hits':
            self.speed += 1
            print('FOUR HITS: increase speed by 1')
        elif event == 'twelve hits':
            self.speed += 1
            print('TWELVE HITS: increase speed by 1')
        elif event == 'orange block':
            if not self.orange_row_hit:
                self.speed += 1
                self.orange_row_hit = True
                print('FIRST ORANGE BLOCK: increase speed by 1')
        else:
            print('INVALID EVENT')

    def reset(self, ball_start_cors):
        """
        Resets the ball after paddle misses
        """
        self.color('white')
        self.goto(ball_start_cors)
        self.orientation = 135
        self.paddle_bounce_angle = 90
        self.setheading(self.orientation)
        time.sleep(3)
