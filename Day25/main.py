"""
Day 25: U.S. States Game
"""
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv('50_states.csv')

df['guessed'] = 0

print(df.head())

game_on = True
while game_on:

    correct_guesses = sum(df["guessed"])
    title_str = f'{correct_guesses}/50 States Correct'
    answer_state = screen.textinput(title=title_str, prompt='What\'s another state\'s name?').lower()

    if answer_state in df['state'].lower():
        print(answer_state)

    if answer_state == 'quit' or correct_guesses == 50:
        game_on = False




screen.exitonclick()