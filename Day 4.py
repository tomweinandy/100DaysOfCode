"""
Day 4: Rock, Paper, Scissors Game
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Begin my code
import random

print('\nHAL 9000 wants to play a game. First person to three points wins. Let\'s begin.')

HAL_score = 0
human_score = 0

while HAL_score + human_score != 3:

    RPS = ['rock', 'paper', 'scissors']
    HAL = random.choice(RPS)

    if HAL == 'rock':
        HAL_hand = rock
    elif HAL == 'scissors':
        HAL_hand = scissors
    else:
        HAL_hand = paper

    human = input('\nSelect \"rock\", \"paper\" or \"scissors\": ').lower()

    if human == 'rock':
        human_hand = rock
    elif human == 'scissors':
        human_hand = scissors
    elif human == 'paper':
        human_hand = paper
    else:
        print('Incorrect entry.\nHAL: \"It can only be attributable to human error.\"')
        continue

    print(f'\nHAL 9000 chose {HAL}\n{HAL_hand}')
    print(f'\nYou chose {human}\n{human_hand}')

    # HAL wins
    if HAL == 'rock' and human == 'scissors':
        HAL_score +=1
        print(f'You loose.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'scissors' and human == 'paper':
        HAL_score +=1
        print(f'You loose.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'paper' and human == 'rock':
        HAL_score +=1
        print(f'You loose.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')

    # Human wins
    if HAL == 'rock' and human == 'paper':
        human_score +=1
        print(f'You win!\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'scissors' and human == 'rock':
        human_score +=1
        print(f'You win!\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'paper' and human == 'scissors':
        human_score +=1
        print(f'You win!\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')

    # Tie
    if HAL == 'rock' and human == 'rock':
        print(f'Tie.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'scissors' and human == 'scissors':
        print(f'Tie.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')
    if HAL == 'paper' and human == 'paper':
        print(f'Tie.\nHAL9000 has {HAL_score} point(s) & you have {human_score} point(s).')

print('Game Over.')
if HAL_score > human_score:
    print('HAL: \"Look, I can see you\'re really upset about this. I honestly think you ought to sit down calmly, '
          'take a stress pill, and think things over.\"')
else:
    print('HAL: \"This conversation can serve no purpose anymore. Goodbye.\"')
