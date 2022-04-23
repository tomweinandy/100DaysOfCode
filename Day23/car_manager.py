import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(360, random.randint(-260, 260))
        # self.backward(STARTING_MOVE_DISTANCE)

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())


class CarManager(Turtle):
    def __init__(self, traffic_rate):
        super().__init__()
        self.cars = []
        self.traffic_rate = traffic_rate

    def add_cars(self):
        if random.random() < self.traffic_rate:
            self.cars.append(Car())

    def green_light(self):
        for car in self.cars:
            car.move()



