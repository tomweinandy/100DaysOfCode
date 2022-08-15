from turtle import Turtle
import time

BALL_START_CORS = (-250, -50)


class Ball(Turtle):
    """
    Ball class that inherits Turtle class
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(BALL_START_CORS)
        self.speed = 1
        self.paddle_bounce_angle = 90
        self.orientation = 315
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
            # self.setheading(self.orientation)

        if wall == 'right':
            if 270 < self.orientation <= 360:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 0 <= self.orientation < 90:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360
            # self.setheading(self.orientation)

        if wall == 'top':
            bounce_angle = 180 + self.paddle_bounce_angle

            if 0 < self.orientation <= 90:
                self.orientation = (self.orientation + bounce_angle) % 360
            elif 90 < self.orientation < 180:
                self.orientation = (self.orientation - bounce_angle) % 360

            # self.setheading(self.orientation)

        if wall == 'bottom':
            if 180 < self.orientation <= 270:
                bounce_angle = 180 + self.paddle_bounce_angle + spin
                self.orientation = (self.orientation + bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle + (2 * spin)

            elif 270 < self.orientation < 360:
                bounce_angle = 180 + self.paddle_bounce_angle - spin
                self.orientation = (self.orientation - bounce_angle) % 360
                self.paddle_bounce_angle = self.paddle_bounce_angle - (2 * spin)

        # Force paddle bounce to be non-negative
        if self.paddle_bounce_angle < 0:
            self.paddle_bounce_angle = abs(self.paddle_bounce_angle)

        self.setheading(self.orientation)
        # print(f'Wall: {wall}, Spin: {spin}, Paddle Bounce Angle: {self.paddle_bounce_angle}, Orientation: {self.orientation}')

    # todo fine tune speed
    def speed_event(self, event):
        if event == 'four hits':
            self.speed += 1.5
            print('FOUR HITS: increase speed by 1')
        elif event == 'twelve hits':
            self.speed += 1.5
            print('TWELVE HITS: increase speed by 1')
        elif event == 'orange block':
            if not self.orange_row_hit:
                self.speed += 1.5
                self.orange_row_hit = True
                print('FIRST ORANGE BLOCK: increase speed by 1')
        else:
            print('INVALID EVENT')

    def reset(self):
        """
        Resets the ball after paddle misses
        """
        time.sleep(1)
        self.color('white')
        # Appears at the same point
        self.goto(BALL_START_CORS)
        self.orientation = 315
        self.paddle_bounce_angle = 90
        self.setheading(self.orientation)
        time.sleep(2)
