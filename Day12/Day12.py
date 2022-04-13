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
df = pd.read_csv('Day12/100movies.csv')
df = df.set_index('Year')

print(logo)
print('Welcome to Circa: The game where you try to guess movie years!')

# Insist the player selects a difficulty level

def difficulty():
    difficulty = ''
    while difficulty not in ['e', 'h']:
        difficulty = input('Choose a difficulty. Type "e" for easy or "h" for hard: ').lower()
        if difficulty == 'e':
            guesses_left = 10
        elif difficulty == 'h':
            guesses_left = 5

    return guesses_left


def format_guess():
    guess = input(f'In what year did * {movie} * come out?: ')

    while type(guess) is not int:
        # guess = guess.replace(' ', '')
        guess = re.sub(r'[^0-9]', '', guess)

        try:
            guess = int(guess)
        except:
            print('Invalid entry.')
            guess = input(f'In what year did * {movie} * come out?: ')

    return guess


play = 'y'
guess = ''


while play == 'y':
    # Select a movie at random
    year = random.choice(df.index)
    movie = df['Movie'][year]

    guesses_left = difficulty()

    while guesses_left != 0:
        guesses_left -= 1

        guess = format_guess()

        if 1919 <= guess <= 2019:
            movie_or_not = df.Movie[guess]
        else:
            movie_or_not = 'No movie on this movie list'

        if guess > year:
            print(f'Not quite. {movie_or_not} came out in {guess}. Your guess was too HIGH. You have {guesses_left} guesses left.')
        elif guess < year:
            print(f'Not quite. {movie_or_not} came out in {guess}. Your guess was too LOW. You have {guesses_left} guesses left.')
        else:
            print('Well done! Get Mr. DeMille, because you\'re ready for your close-up.')
            break

    else:
        print(f'The correct answer is {year}. "Game over, man!"')

    play = input('\n"I wanna play a game." Type "y" to continue or "n" to stop: ')

print('"I think this is the beginning of a beautiful friendship."')



