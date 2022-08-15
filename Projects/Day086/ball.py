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
        self.speed = 2
        self.paddle_bounce_angle = 90
        self.orientation = ball_start_orientation
        self.paddle_hits = 0
        self.ceiling_hit = False
        self.orange_row_hit = False

        self.setheading(self.orientation)

    def bounce(self, wall, spin=0):
        """
        :param wall: 'top', 'bottom', 'left', 'right'
        :param spin:
        :return:
        """

        if wall == 'left':
            if 90 < self.orientation <= 180:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 180 < self.orientation < 270:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360

        if wall == 'right':
            if 270 < self.orientation <= 360:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 0 <= self.orientation < 90:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360

        if wall == 'top':
            bounce_angle = 180 + self.paddle_bounce_angle

            if 0 < self.orientation <= 90:
                self.orientation = (self.orientation + bounce_angle) % 360
            elif 90 < self.orientation < 180:
                self.orientation = (self.orientation - bounce_angle) % 360

        if wall == 'bottom':
            if 180 < self.orientation <= 270:
                bounce_angle = 180 + self.paddle_bounce_angle + spin
                self.orientation = (self.orientation + bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle + (2 * spin)

            if 270 < self.orientation < 360:
                bounce_angle = 180 + self.paddle_bounce_angle - spin
                self.orientation = (self.orientation - bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle - (2 * spin)

            # Prevent paddle bounce angle from being larger than 170 degrees
            if self.paddle_bounce_angle > 170:
                self.paddle_bounce_angle = 170

        # Force paddle bounce to be between 0 and 170 degrees
        if self.paddle_bounce_angle < 0:
            self.paddle_bounce_angle = abs(self.paddle_bounce_angle)
        if self.paddle_bounce_angle > 170:
            self.paddle_bounce_angle = 170

        self.setheading(self.orientation)
        print(f'Wall: {wall}, Spin: {spin}, Paddle Bounce Angle: {self.paddle_bounce_angle}, Orientation: {self.orientation}')

    def speed_event(self, event):
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
        time.sleep(1)
        self.color('white')
        # Appears at the same point
        self.goto(ball_start_cors)
        self.orientation = 135
        self.paddle_bounce_angle = 90
        self.setheading(self.orientation)
        time.sleep(2)
