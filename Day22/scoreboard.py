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
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard after a point is scored
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))

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

    def win(self, player):
        """
        Announces which player won
        :param player: 'left' or 'right'
        """
        self.goto(0, 0)
        self.write(f'{player.title()} Player wins!', align='center', font=('Courier', 36, 'normal'))
