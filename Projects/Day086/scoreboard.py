import turtle


class Scoreboard(turtle.Turtle):
    """
    Scoreboard class inherited from the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 2
        self.points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard after a point is scored
        """
        self.clear()
        self.goto(-400, 340)
        self.write(self.points, align='center', font=('Courier', 40, 'normal'))
        self.goto(400, 340)
        self.write(self.lives, align='center', font=('Courier', 40, 'normal'))

    def point(self, player):
        """
        Assigns a point to a player
        :param player: 'left' or 'right'
        """
        if player == 'left':
            self.left_score += 1
        elif player == 'right':
            self.right_score += 1
        self.update_scoreboard()

    def end_round(self, outcome):
        """
        Announces which player won
        :param player: 'left' or 'right' #todo document
        """
        if outcome == 'win':
            self.goto(0, 0)
            self.write('Player wins!', align='center', font=('Courier', 36, 'normal'))
        elif outcome == 'lose':
            self.goto(0, 0)
            self.write('Player loses.', align='center', font=('Courier', 36, 'normal'))
        else:
            # todo add level up result
            pass

