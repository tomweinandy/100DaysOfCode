from turtle import Turtle

with open('data.txt', 'r') as file:
    data = file.read()
    previous_high_score_string = data.split(':')
    print(previous_high_score_string)
    previous_high_score = int(previous_high_score_string[1])

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = previous_high_score
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

