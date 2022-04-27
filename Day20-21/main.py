"""
Day 20-21: Snake Game
"""
import turtle
import snake
import time
import food
import scoreboard

# todo better document
# todo test snek more
# todo add high scores for each difficulty


# Set initial conditions
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakes on a Plane')
screen.tracer(0)  # only updates on screen.update()

# My pet snake is named "snek"
snek = snake.Snake()
difficulty = scoreboard.difficulty()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

# Begin the game
game_on = True
while game_on:
    # "Listens" for keystrokes
    screen.listen()
    screen.onkey(snek.turn_up, "Up")
    screen.onkey(snek.turn_down, "Down")
    screen.onkey(snek.turn_left, "Left")
    screen.onkey(snek.turn_right, "Right")

    screen.update()
    time.sleep(difficulty)
    snek.move()

    # Detect collision with food
    if snek.head.distance(food) <= 15:
        snek.extend()
        food.refresh()
        scoreboard.refresh()

    # Detect collision with wall
    if snek.head.xcor() > 300 or snek.head.xcor() < -300 or snek.head.ycor() > 300 or snek.head.ycor() < -280:
        game_on = snake.play_again()
        scoreboard.reset()
        snek.reset()

    # Detect collision with tail
    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 5:
            game_on = snake.play_again()
            scoreboard.reset()
            snek.reset()

screen.exitonclick()
