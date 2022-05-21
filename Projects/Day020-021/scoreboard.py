import turtle
import json

with open('data.txt', 'r') as file:
    data = file.read()
    score_dict = json.loads(data)


class Scoreboard(turtle.Turtle):
    """
    Defines new scoreboard class that inherits properties of Turtle class
    """
    def __init__(self):
        super().__init__()
        screen = turtle.Screen()
        # Sets the pause_length according to the difficulty mode
        mode = screen.textinput(title='Mode', prompt='Set level of difficulty (easy/normal/hard): ').lower()
        if mode == 'easy':
            self.pause_length = 0.15
        elif mode == 'hard':
            self.pause_length = 0.05
        else:
            mode = 'normal'
            self.pause_length = 0.1
        self.mode = mode
        self.high_score = score_dict[self.mode][0]
        self.high_scorer = score_dict[self.mode][1]
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.score}   High Score: {self.high_score} ({self.high_scorer})',
                   align='center',
                   font=('Arial', 24, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        """
        Updates the scoreboard with the new score and current highscore/r
        """
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score} ({self.high_scorer})',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def refresh(self):
        """
        Adds a point to the current score
        :return:
        """
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score} ({self.high_scorer})',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def reset(self):
        """
        Checks if the current score is a high score in the associated difficulty mode.
        If so, it will write the new high score/r to data.txt and update the scoreboard.
        """
        screen = turtle.Screen()
        if self.score > self.high_score:
            self.high_score = self.score

            self.high_scorer = screen.textinput(title='New High Score!', prompt='Enter your name: ')
            score_dict[self.mode] = [self.high_score, self.high_scorer]
            with open('data.txt', 'w') as outfile:
                json.dump(score_dict, outfile)
        self.score = 0
        self.update_scoreboard()
