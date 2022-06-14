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
        distance_above = abs(car.position()[1] - player.position()[1])
        distance_below = abs(player.position()[1] - car.position()[1])

        if x_distance < 19 and distance_above < 20:
            scoreboard.game_over(traffic_rate)
            game_on = False
            print(f'ABOVE x_distance: {x_distance}, distance_above: {distance_above}, distance_below: {distance_below}')

        if x_distance < 19 and distance_below < 19:
            scoreboard.game_over(traffic_rate)
            game_on = False
            print(f'BELOW x_distance: {x_distance}, distance_above: {distance_above}, distance_below: {distance_below}')

    if player.ycor() > FINISH_LINE_Y:
        # scoreboard.clear()
        car_manager.increase_traffic()
        player.reset_position()
        scoreboard.level_up(traffic_rate)
        # print(f'Traffic: {round(car_manager.traffic_rate, 2)}')

    # todo test sensitivity
    # todo document
    # todo fix writing over traffic


screen.exitonclick()
