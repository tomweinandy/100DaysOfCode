"""
Day 23: Turtle Crossing Game
"""
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Why did the turtle cross the road?')
screen.tracer(0)

# Initialize classes
player = Player()
scoreboard = Scoreboard()
scoreboard.hideturtle()
car_manager = CarManager(0.1)
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
    traffic_rate = round(car_manager.traffic_rate, 2)
    scoreboard.write_traffic(traffic_rate)

    for car in car_manager.cars:
        x_distance = abs(car.position()[0] - player.position()[0])
        y_distance = abs(car.position()[1] - player.position()[1])

        if x_distance < 10 and y_distance < 20:
            scoreboard.game_over(traffic_rate)
            game_on = False

    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level_up(traffic_rate)
        car_manager.increase_traffic()
        player.reset_position()
        # print(f'Traffic: {round(car_manager.traffic_rate, 2)}')

    # todo add traffic rate
    # todo test sensitivity
    # todo document


screen.exitonclick()