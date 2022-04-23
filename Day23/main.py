import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager(1)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_cars()
    car_manager.green_light()


    # todo add turtle movement function
    # todo detect car collision
    # todo detect when the turtle crosses the finish line
    # todo advance to next level and tune car speed
    #

screen.exitonclick()