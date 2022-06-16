from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 260)
RULES_POSITION = (-50, 260)
GAME_OVER_POSITION = (125, 260)
TRAFFIC_POSITION = (-280, -280)


class Scoreboard(Turtle):
    def __init__(self):
        """
        Use the turtle superclass to create a scoreboard module that keeps track of levels.
        """
        super().__init__()
        self.level = 1
        self.penup()
        self.write_level()
        self.goto(RULES_POSITION)
        self.write('Turtles never look back', font=FONT)

    def level_up(self):
        """
        Increase the level by one
        """
        self.level += 1
        self.clear()
        self.write_level()
        self.write_traffic()

    def game_over(self):
        """
        Ends the game and prints "game over"
        """
        self.clear()
        self.write_traffic()
        self.write_level()
        self.goto(GAME_OVER_POSITION)
        self.write('Game Over.', font=FONT)

    def write_traffic(self):
        """
        Posts the current traffic rate (begins at 0.1 and then increases by 10% each level)
        """
        self.goto(TRAFFIC_POSITION)
        traffic_rate = 0.1 * (1.1 ** (self.level-1))
        traffic_rate_rounded = round(traffic_rate, 2)
        self.write(f'Traffic Rate: {traffic_rate_rounded}', font=FONT)

    def write_level(self):
        """
        Posts the current level
        """
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)
