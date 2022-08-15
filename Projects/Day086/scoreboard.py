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
        Updates the scoreboard after paddle misses or block is broken
        """
        self.clear()
        self.goto(-350, 340)
        self.write(self.points, align='center', font=('Courier', 40, 'normal'))
        self.goto(400, 340)
        self.write(self.lives, align='center', font=('Courier', 40, 'normal'))

    def game_over(self):
        self.goto(0, -100)
        self.write('Game Over.', align='center', font=('Courier', 36, 'normal'))


