from turtle import Turtle
import player

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 260)
RULES_POSITION = (-50, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)

        self.goto(RULES_POSITION)
        self.write('Turtles never look back', font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f'Level: {self.level}', font=FONT)
