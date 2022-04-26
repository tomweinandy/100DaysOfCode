from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 260)
RULES_POSITION = (-50, 260)
GAME_OVER_POSITION = (125, 260)
TRAFFIC_POSITION = (-280, -280)
# TRAFFIC_POSITION = (-280, 260) #todo

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)

        self.goto(RULES_POSITION)
        self.write('Turtles never look back', font=FONT)

    def level_up(self, traffic_rate):
        self.level += 1
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)
        self.write_traffic(traffic_rate)

    def game_over(self, traffic_rate):
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)
        self.goto(GAME_OVER_POSITION)
        self.write('Game Over.', font=FONT)
        self.write_traffic(traffic_rate)

    def write_traffic(self, traffic_rate):
        self.goto(TRAFFIC_POSITION)
        self.write(f'Traffic Rate: {traffic_rate}', font=FONT)
