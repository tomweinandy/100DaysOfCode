"""
Day 7: Hangman Game
"""
import random
import requests
import re
import art as art, words as words

print(f'\nWelcome to...\n{art.logo}\n')

choice = input('Do you want to play? ').lower()

while choice != 'n':
    # Select word from list
    if choice == 'after dark':
        # Get new word list
        target_url = 'https://www.cs.cmu.edu/~biglou/resources/bad-words.txt'
        response = requests.get(target_url)
        after_dark = response.text.split('\n')

        # Remove non-latin letters and blanks ('if i')
        after_dark = [re.sub(r'[^a-z]', '', i) for i in after_dark if i]

        # Select a bad word
        chosen_word = random.choice(after_dark)

    else:
        # Select a word
        chosen_word = random.choice(words.word_list)

    print('\nGreat, let\'s begin! The rules are simple: stay alive.\n')

    # Build and display the hidden word
    display = []
    for letter in chosen_word:
        display.append('_')
    print(display)

    # Define lives and empty string of guessed letters
    lives = len(art.stages)
    guesses = ''

    # Continue while there are blanks left in word
    while '_' in display:
        if lives != 0:
            if lives == 1:
                life_or_lives = 'life'
            else:
                life_or_lives = 'lives'

            guess = input("Guess a letter: ").lower()
            guesses += guess

            # Tell player if they were correct
            if guess in chosen_word:
                print(f'Correct! You have {lives} {life_or_lives} left.')
            else:
                lives -= 1
                print(art.stages[lives])
                print(f'Ouch, not quite. You have {lives} {life_or_lives} left.')

            # Update display with correctly guessed letters
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess

            print(f'Guesses: {guesses} \n{display}\n')

        # Game Over, Man
        else:
            print(art.stages[lives])
            print(f'The word was {chosen_word}')
            print('As James Franco would say, \"First time?\" Game Over.')
            break

    choice = input('Play again? (y/n) ').lower()
