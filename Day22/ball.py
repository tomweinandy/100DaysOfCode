from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.speed = 1

    def move(self):
        new_x = self.xcor() + 10*self.x_direction
        new_y = self.ycor() + 10*self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, x=False, y=False):
        if x:
            self.x_direction *= -1
        if y:
            self.y_direction *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(x=True, y=True)

    def increase_speed(self):
        self.speed *= 0.9

    def reset_speed(self):
        self.speed = 1

