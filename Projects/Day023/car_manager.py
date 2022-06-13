import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        """
        A car class inheriting the turtle class to create cars the form traffic
        """
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(360, random.randint(-240, 240))

    def move(self):
        """
        Moves the car objects left across the screen
        """
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())


class CarManager(Turtle):
    """
    A car class inheriting the turtle class to manage traffic patterns
    """
    def __init__(self, traffic_rate):
        super().__init__()
        self.cars = []
        self.traffic_rate = traffic_rate

    def add_cars(self):
        """
        Increases the number of cars
        """
        if random.random() < self.traffic_rate:
            self.cars.append(Car())

    def green_light(self):
        """
        Starts traffic
        """
        for car in self.cars:
            car.move()

    def increase_traffic(self):
        """
        Increments the traffic rate by 10%
        """
        self.traffic_rate *= 1.1
