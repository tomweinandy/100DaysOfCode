"""
Day 14: Higher Lower Game
"""
# Inspired by the original of the same name: http://www.higherlowergame.com

from art import logo, vs
from game_data import data
import random

keep_playing = True

while keep_playing:

    # Set game initial conditions
    score = 0
    current_game = True
    print(logo)

    while current_game:
        # Select a data point for Comparison A
        a = random.choice(data)

        # Select a data point for Comparison B (can't be same as A)
        b = random.choice(data)
        while a == b:
            b = random.choice(data)

        a_count = a['follower_count']
        b_count = b['follower_count']

        print(f"Compare A: {a['name']}, the {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, the {b['description']}, from {b['country']}")

        # Only accept a guess of 'a' or 'b'
        guess = ''
        while guess not in ['a', 'b']:
            guess = input('Who has more followers? Type "A" or "B": ').lower()

        percent_difference_a = round(100 * (a_count - b_count) / b_count)
        percent_difference_b = round(100 * (b_count - a_count) / a_count)

        if guess == 'a':
            # If correct
            if a_count >= b_count:
                score += 1
                print(f"Well done! {a['name']} has {percent_difference_a}% more followers than {b['name']}."
                      f" You have {score} points.\n")
            # If incorrect
            else:
                print(f"Too bad. {b['name']} has {percent_difference_b}% more followers than {a['name']}. "
                      f"Final Score: {score}.\n")
                current_game = False

        if guess == 'b':
            # If correct
            if a_count <= b_count:
                score += 1
                print(f"Well done! {b['name']} has {percent_difference_b}% more followers than {a['name']}."
                      f" You have {score} points.\n")
            # If incorrect
            else:
                print(f"Too bad. {a['name']} has {percent_difference_a}% more followers than {b['name']}. "
                      f"Final Score: {score}.\n")
                current_game = False

    # Ask if player wants to play again
    play_again = ''
    while play_again not in ['y', 'n']:
        play_again = input('Want to play again? Type "y" for yes or "n" for no: ').lower()

        if play_again == 'n':
            keep_playing = False
