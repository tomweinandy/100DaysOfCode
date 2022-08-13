from turtle import Turtle
import time
import random

BALL_START_CORS = (-250, 0)

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
        self.speed = 0.5
        self.paddle_bounce_angle = 90
        self.orientation = 315
        self.paddle_hits = 0
        self.paused = True #todo remove
        self.ceiling_hit = False
        self.orange_row_hit = False

        # Sets x and y direction as positive (i.e., is moving in northeast direction)
        self.x_direction = 1
        self.y_direction = -1

        self.setheading(self.orientation)

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
        # new_x = self.xcor() + (10 * self.x_direction) #* (180 - self.bounce_angle)/90
        # new_y = self.ycor() + (10 * self.y_direction)
        # self.goto(new_x, new_y)
        self.forward(10)

    def bounce(self, wall):
        """

        :param wall: 'top', 'bottom', 'left', 'right'
        :return:
        """
        if wall == 'left':
            if 90 < self.orientation < 180:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 180 < self.orientation < 270:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360
            self.setheading(self.orientation)

        if wall == 'right':
            if 270 < self.orientation < 360:
                self.orientation = (self.orientation - self.paddle_bounce_angle) % 360
            elif 0 < self.orientation < 90:
                self.orientation = (self.orientation + self.paddle_bounce_angle) % 360
            self.setheading(self.orientation)

        if wall == 'top':
            bounce_angle = 180 + self.paddle_bounce_angle

            if 0 < self.orientation <= 90:
                self.orientation = (self.orientation + bounce_angle) % 360
            elif 90 < self.orientation < 180:
                self.orientation = (self.orientation - bounce_angle) % 360

            self.setheading(self.orientation)

        if wall == 'bottom':
            bounce_angle = 180 + self.paddle_bounce_angle

            if 180 < self.orientation <= 270:
                self.orientation = (self.orientation + bounce_angle) % 360
            elif 270 < self.orientation < 360:
                self.orientation = (self.orientation - bounce_angle) % 360

            self.setheading(self.orientation)

        print(self.orientation)



    def bounce_old(self, x_reflect=False, y_reflect=False, hit_paddle=False, segement_hit=0):
        """
        Flips the x or y direction depending on what it bounces off of
        :param x_reflect: True when bouncing off the left or right of an object
        :param y_reflect: True when bouncing off the top or bottom of an object
        :param paddle_placement: The section of the paddle hit from 0-1 (ie, left-most to right-most). Determines amount
        spin to add to the ball where 0.5 (middle of paddle) is none and the outermost ends change spin by 44%.
        """
        if x_reflect:
            self.ceiling_hit = True #todo fix
            self.x_direction *= -1
            # self.random_jitter() #todo remove jitter everywhere
            #todo add count if it hits the paddle

        # Shows conversion between placement on paddle and amount of spin
        spin_dict = {0: -20,
                     1: -15,
                     2: -10,
                     3: -5,
                     4: 5,
                     5: 10,
                     6: 15,
                     7: 20}

        if y_reflect:
            self.y_direction *= -1
            # self.orientation = self.orientation - self.bounce_angle
            # self.setheading(self.orientation)

            if hit_paddle:
                spin = spin_dict[segement_hit] * self.x_direction
                old_bounce_angle = self.bounce_angle
                new_bounce_angle = old_bounce_angle + spin
                if 0 < new_bounce_angle < 180:
                    self.right(spin)
                    self.bounce_angle = new_bounce_angle
                    print('spin', spin)
            print('bounce angle', self.bounce_angle)


            # net_distance = paddle_placement - 0.5   # rightward distance from middle of paddle
            # spin = (1 + net_distance)
            #
            # old_orientation = self.orientation
            # new_orientation = old_orientation + spin
            #
            # if -80 < new_orientation < 80:
            #     self.right(spin)
            #     self.orientation = new_orientation
            #
            # print(self.orientation)


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
        # Appears at the same point
        self.goto(BALL_START_CORS)
        self.x_direction = 1
        self.y_direction = -1
        self.orient = 315
        self.setheading(self.orient)
        time.sleep(2)
