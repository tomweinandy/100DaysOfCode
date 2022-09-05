import turtle

ISLAND_OF_MISFIT_TOYS = (-1000, 1000)


class Scoreboard(turtle.Turtle):
    """
    Scoreboard class inherited from the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.plus100 = None
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.lives_since_last_update = 2
        self.points = 0
        self.invaders_hit = 0
        self.timer = 0
        self.time_when_defender_last_hit = 0
        self.time_when_last_mothership_appeared = -800
        self.time_when_last_points_displayed = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard after life lost or points gained
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


def show_points(color_type, position):
    """
    Prints the number of points awarded based on the color (motherships are yellow, invaders are white).
    """
    pointer = turtle.Turtle()
    pointer.penup()
    pointer.goto(position)
    pointer.color(color_type)

    # Prints different amount based on if the white invader was hit or the yellow mothership
    if color_type == 'yellow':
        pointer.write('+100', align='center', font=('Courier', 14, 'normal'))
    elif color_type == 'white':
        pointer.write('+10', align='center', font=('Courier', 14, 'normal'))

    # Moves turtle object away (but leaves text)
    pointer.goto(ISLAND_OF_MISFIT_TOYS)
    return pointer
