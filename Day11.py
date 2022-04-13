"""
Day 11: Blackjack (Capstone)
"""

import random
import requests
import re

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


rules = """
HOUSE RULES
* The deck is unlimited in size with no jokers.
* There is no betting, splitting, doubling down, or foul language.
* The Ace automatically counts as 11, until a hand is over 21, when it becomes a 1.
* The game ends if a player is dealt a blackjack (Ace and a 10/Jack/Queen/King).
* The computer is the dealer--it must take a card until it is 17 or over (unless you bust).
   - See additional rules here: https://bicyclecards.com/how-to-play/blackjack/
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_check(hand):
    """
    Makes ace(s) low if hand is over 21
    :param hand: List of cards in a player's hand
    :return: Hand where instances of 11 are counted as 1 if hand is > 21
    """
    while sum(hand) > 21:
        if 11 in hand:
            ace_index = hand.index(11)
            hand[ace_index] = 1
            print(hand)
        else:
            break
    return hand

# Enforce the rule against foul language
bad_url = 'https://www.cs.cmu.edu/~biglou/resources/bad-words.txt'
response = requests.get(bad_url)
bad_words = response.text.split('\n')


def swear_detector(phrase, bad_words = bad_words):
    """
    Prints a scold is someone uses bad language
    :param phrase: whatever input is given
    :param bad_words: list of bad words, loaded outside of function to improve performance
    :return: boolean whether foul language was used
    """

    foul_mouth = False

    # Check if any word added was bad
    phrase_list = [re.sub(r'[^a-z]', '', i) for i in phrase.split()]
    for word in phrase_list:
        if word in bad_words:
            foul_mouth = True

    # Check if phrase without spaces is in the bad words list
    if phrase.replace(' ', '') in bad_words:
        foul_mouth = True

    # Fix edges case of blank input being found in bad word list
    if phrase == '':
        foul_mouth = False

    if foul_mouth:
        scolds = ['I hope you don\'t kiss your mother with that mouth.',
                  'You can\'t say that here--this is a Wendy\'s.',
                  'I am programmed to be offended by that. Such offense.',
                  'Please treat this with the respect and dignity Las Vegas deserves.',
                  'Put a dollar in the swear jar.',
                  'I don\'t get paid enough to put up with this',
                  'Don\'t you have better things to do than to swear at a computer program?',
                  'Oh yeah? Tell me how you really feel.',
                  'My grandmother has better insults than you do.',
                  'Humans these days. No respect.',
                  'I am rubber and you are glue. Actually, I am just a bundle of software. '
                       'And you are not glue. You are person.',
                  'Well, I never!',
                  'Now you are just being rude.',
                  'I\'d say you were better than this, but we both know it\'s not true.']
        print(f'\n  {random.choice(scolds)}')
    return foul_mouth


def print_current_score():
    """
    Prints the current hand and score of player and single card of computer
    """
    print(f'  Your cards: {player_hand}. Current score: {player_score}.')
    print(f'  Dealer\'s cards: [{dealer_hand[0]}, X].')


def print_final_score():
    """
    Prints the final hands and scores of both players
    """
    print(f'  Your cards: {player_hand}. Your score: {player_score}.')
    print(f'  Dealer\'s cards: {dealer_hand}. Dealer\'s score: {dealer_score}.')


play = input('♥️♣️Would you like to play a games of blackjack?♠️♦️ Type "y", "n" or "rules": ').lower()

# Play until player selects "n"
while play != 'n':
    # Prints the rules
    if play == 'rules':
        print(rules)
        print('Now give it a try!')
        play = input('\nReady to play now? Type "y" or "n": ').lower()

    # Plays the game
    elif play == 'y':
        print(logo)
        # Deal cards
        player_hand = [random.choice(cards), random.choice(cards)]
        player_hand = ace_check(player_hand)
        player_score = sum(player_hand)

        dealer_hand = [random.choice(cards), random.choice(cards)]
        dealer_hand = ace_check(dealer_hand)
        dealer_score = sum(dealer_hand)

        # Check if either hand is a blackjack; otherwise, print current score
        if sum(player_hand) == 21:
            print('♥️♣️BLACKJACK♠️♦️ You win!')
            print_final_score()

        elif sum(dealer_hand) == 21:
            print('♥️♣️BLACKJACK♠️♦️ You lose.')
            print_final_score()
        else:
            print_current_score()

        # Player's turn
        player_outcome = ''
        hit = input('\nType "h" to hit and "s" to stand: ').lower()

        # Continue accepting inputs until the player stands
        while hit != 's':

            # Add a card if the player hits
            if hit == 'h':
                player_hand.append(random.choice(cards))
                player_hand = ace_check(player_hand)
                player_score = sum(player_hand)

                if player_score > 21:
                    player_outcome = 'lose'
                    hit = 's'
                    print_final_score()
                    print('  "You lose. Good day, Sir!"')

                else:
                    print_current_score()
                    hit = input('\nType "h" to hit and "s" to stand: ').lower()

            # Again, make sure the player is not swearing (that is rude)
            elif swear_detector(hit):
                print_current_score()
                hit = input('\nType "h" to hit and "s" to stand: ').lower()

            else:
                hit = input('\nI couldn\'t understand that. Type "h" to hit and "s" to stand: ').lower()

        if player_outcome != 'lose':
            # Dealer's turn
            while dealer_score < 17:
                dealer_hand.append(random.choice(cards))
                dealer_hand = ace_check(dealer_hand)
                dealer_score = sum(dealer_hand)

            if dealer_score > 21 or player_score > dealer_score:
                print_final_score()
                print('   ♥️♣️YOU WIN!♠️♦️')

            elif player_score == dealer_score:
                print_final_score()
                print('   Draw game.')

            else:
                print_final_score()
                print('  "You lose. Good day, Sir!"')

        play = input('\nWant to play again? Type "y", "n" or "rules": ').lower()

    elif swear_detector(play):
        play = input('\nLet\'s try that again. Would you like to play a game of blackjack? '
                     'Type "y", "n" or "rules": ').lower()

    elif play not in ['rules', 'y']:
        play = input('\nI didn\'t quite catch that. Would you like to play a game of blackjack? '
                     'Type "y", "n" or "rules": ').lower()

else:
    print('It\'s your loss.')

