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
        self.lives = 3
        self.lives_since_last_update = 2
        self.points = 0
        self.invaders_hit = 0
        self.timer = 0
        self.time_when_defender_last_hit = 0
        self.time_when_last_mothership_appeared = -900 #todo change to 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard after paddle misses (life lost) or block is broken (points gained)
        """
        self.clear()
        self.goto(-350, 340)
        self.write(self.points, align='center', font=('Courier', 40, 'normal'))
        self.goto(330, 340)
        self.write(self.lives, align='center', font=('Courier', 40, 'normal'))

    def game_over(self):
        """
        Prints 'game over'
        """
        self.goto(0, -100)
        self.write('Game Over.', align='center', font=('Courier', 36, 'normal'))

    def game_won(self):
        """
        Prints 'you win'
        """
        self.goto(0, 0)
        self.write('You win!', align='center', font=('Courier', 36, 'normal'))
