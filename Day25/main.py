"""
Day 25: U.S. States Game
"""
import turtle
import pandas as pd


def print_state(data, state):
    answer_data = data[data['state'] == state]
    location = (answer_data['x'], answer_data['y'])

    t = turtle.Turtle()
    t.penup()
    t.goto(location)
    t.write(state)


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

    correct_guesses = sum(df['guessed'])
    title_str = f'{correct_guesses}/50 States Correct'
    answer_state = screen.textinput(title=title_str, prompt='What\'s another state\'s name?')
    answer_state = answer_state.lower().title()

    answer_df = df[df['state'] == answer_state]
    print(answer_df)

    if len(answer_df) > 0:
        correct_answer_index = answer_df.index[0]
        df.at[correct_answer_index, 'guessed'] = 1
        # print_state(df, answer_state)



    print(df[df['state'] == answer_state])



    if answer_state == 'quit' or correct_guesses == 50:
        game_on = False




screen.exitonclick()