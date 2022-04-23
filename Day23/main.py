import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player and traffic
player = Player()
car_manager = CarManager(0.5)
car_manager.hideturtle()

# Add player movement
screen.listen()
screen.onkey(player.move, 'Up')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_cars()
    car_manager.green_light()

    for car in car_manager.cars:
        x_distance = abs(car.position()[0] - player.position()[0])
        y_distance = abs(car.position()[1] - player.position()[1])

        if x_distance < 5 and y_distance < 20:
            game_on = False

    # todo advance to next level and tune car speed
    # todo fine tune collision distance

screen.exitonclick()