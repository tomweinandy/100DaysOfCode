from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.speed = 1
        self.paused = True

    def pause(self):
        if self.paused:
            self.paused = False
            print('pause off')
        else:
            self.paused = True
            print('pause on')

    def move(self):
        new_x = self.xcor() + 10*self.x_direction
        new_y = self.ycor() + 10*self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, x=False, y=False):
        if x:
            self.x_direction *= -1
            self.turn(10)
        if y:
            self.y_direction *= -1

    def increase_speed(self):
        self.speed *= 0.9

    def reset(self):
        time.sleep(1)
        self.speed = 1
        self.color('white')
        # Appears within a random point on the y-axis
        self.goto(0, random.randint(-250, 250))
        self.bounce(x=True, y=True)


