"""
Day 12: Movie Guesser
"""
import pandas as pd
import random
import re

logo = """                                                                                                           
                              ______  __  .______        ______      ___      
                             /      ||  | |   _  \      /      |    /   \     
                            |  ,----'|  | |  |_)  |    |  ,----'   /  ^  \    
                            |  |     |  | |      /     |  |       /  /_\  \   
                            |  `----.|  | |  |\  \----.|  `----. /  _____  \  
                             \______||__| | _| `._____| \______|/__/     \__\ 
                                  _     _                                  _                                   
  __ _   _  _   ___   ___  ___   | |_  | |_    ___     _ __    ___  __ __ (_)  ___     _  _   ___   __ _   _ _ 
 / _` | | || | / -_) (_-< (_-<   |  _| | ' \  / -_)   | '  \  / _ \ \ V / | | / -_)   | || | / -_) / _` | | '_|
 \__, |  \_,_| \___| /__/ /__/    \__| |_||_| \___|   |_|_|_| \___/  \_/  |_| \___|    \_, | \___| \__,_| |_|  
 |___/                                                                                 |__/                    
"""

# Load list of 100 movies
df = pd.read_csv('100movies.csv')
df = df.set_index('Year')

print('\nWelcome to Circa: The game where you try to guess movie years! '
      '"Fasten your seatbelts. It\'s going to be a bumpy night."')

# Define some helper functions
def difficulty():
    """
    Sets the level of difficulty based on the player input
    :return: 10 guesses if easy ("e") or 5 guesses if hard ("h")
    """
    difficulty = ''
    # Force input to be one of two options
    while difficulty not in ['e', 'h']:
        difficulty = input('Choose a difficulty. Type "e" for easy or "h" for hard: ').lower()
        if difficulty == 'e':
            guesses_left = 10
        elif difficulty == 'h':
            guesses_left = 5

    return guesses_left


def format_guess():
    """
    Asks user for guess and formats or asks again until valid input
    :return: integer
    """
    guess = input(f'In what year did {movie} come out?: ')

    while type(guess) is not int:
        # Remove non-numeric characters
        guess = re.sub(r'[^0-9]', '', guess)

        try:
            guess = int(guess)
        except:
            print('Invalid entry. "What we\'ve got here is a failure to communicate."')
            guess = input(f'In what year did {movie} come out?: ')

    return guess


play = 'y'
guess = ''

# Begins game
while play == 'y':
    print(logo)

    # Select a movie at random
    year = random.choice(df.index)
    movie = df['Movie'][year]

    # Player selects difficulty
    guesses_left = difficulty()

    # Plays until guesses run out
    while guesses_left != 0:
        guesses_left -= 1

        # Player makes a guess
        guess = format_guess()

        # Shows a movie that came out in the guessed year (if exists)
        if 1919 <= guess <= 2019:
            movie_or_not = df.Movie[guess]
        else:
            movie_or_not = 'No movie on this movie list'

        # Checks guess
        if guess > year:
            print(f'"You talking to me?" {movie_or_not} came out in {guess}. Your guess was too HIGH. '
                  f'You have {guesses_left} guesses left.')
        elif guess < year:
            print(f'"You talking to me?" {movie_or_not} came out in {guess}. Your guess was too LOW. '
                  f'You have {guesses_left} guesses left.')
        else:
            print(f'Correct! {movie} came out in {year}. "Show me the money!"')
            break

    # When guesses run out
    else:
        print(f'The correct answer is {year}. "Game over, man!"')

    play = input('\n"I wanna play a game." Type "y" to continue or "n" to stop: ')

    if play == 'y':
        print('"I\'ll be back."')

print('"I think this is the beginning of a beautiful friendship."')
