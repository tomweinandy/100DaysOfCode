from turtle import Turtle, Screen
import json

with open('data.txt', 'r') as file:
    data = file.read()
    score_dict = json.loads(data)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score_easy = score_dict['easy'][0]
        self.high_scorer_easy = score_dict['easy'][1]
        self.high_score_normal = score_dict['normal'][0]
        self.high_scorer_normal = score_dict['normal'][1]
        self.high_score_hard = score_dict['hard'][0]
        self.high_scorer_hard = score_dict['hard'][1]
        # self.high_score = previous_high_score
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.score}   High Score: {self.high_score_normal} ({self.high_scorer_normal})',
                   align='center',
                   font=('Arial', 24, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score_normal} ({self.high_scorer_normal})',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score_normal} ({self.high_scorer_normal})',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score_normal:
            self.high_score_normal = self.score

            score_dict['High Score (normal mode)'] = self.high_score_normal
            with open('data.txt', 'w') as outfile:
                json.dump(score_dict, outfile)

        self.score = 0
        self.update_scoreboard()


def difficulty():
    screen = Screen()
    mode = screen.textinput(title='Mode', prompt='Set level of difficulty (easy/normal/hard): ').lower()
    if mode == 'easy':
        pause_length = 0.15
    elif mode == 'hard':
        pause_length = 0.05
    else:
        pause_length = 0.1
    return pause_length