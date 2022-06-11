from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 260)
RULES_POSITION = (-50, 260)
GAME_OVER_POSITION = (125, 260)
TRAFFIC_POSITION = (-280, -280)
# TRAFFIC_POSITION = (-280, 260) #todo


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

    def level_up(self, traffic_rate):
        """
        Increase the level by one
        :param traffic_rate: The rate of traffic flow (begins at 0.1)
        """
        self.level += 1
        self.clear()
        self.write_level()
        self.write_traffic(traffic_rate)

    def game_over(self, traffic_rate):
        """
        Ends the game and prints "game over"
        :param traffic_rate: The rate of traffic flow (begins at 0.1)
        """
        self.clear()
        self.write_level()
        self.write_traffic(traffic_rate)
        self.goto(GAME_OVER_POSITION)
        self.write('Game Over.', font=FONT)

    def write_traffic(self, traffic_rate):
        """
        Posts the current traffic rate
        :param traffic_rate: The rate of traffic flow (begins at 0.1)
        """
        self.goto(TRAFFIC_POSITION)
        self.write(f'Traffic Rate: {traffic_rate}', font=FONT)

    def write_level(self):
        """
        Posts the current level
        """
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)
