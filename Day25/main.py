"""
Day 25: U.S. States Game
"""
import turtle
import pandas as pd


def print_state(data, state):
    answer_data = data[data['state'] == state]
    answer_idx = answer_data.index[0]
    x = answer_data['x'][answer_idx]
    y = answer_data['y'][answer_idx]

    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.write(state)
    t.goto(1000, 1000)


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)
# screen.update()
turtle.shape(image)

df = pd.read_csv('50_states.csv')

df['guessed'] = 0

print(df.head())

game_on = True
while game_on:

    screen.update()

    correct_guesses = sum(df['guessed'])
    title_str = f'{correct_guesses}/50 States Correct'
    answer_state = screen.textinput(title=title_str, prompt='What\'s another state\'s name?')
    answer_state = answer_state.lower().title()

    answer_df = df[df['state'] == answer_state]
    print(answer_df)

    if len(answer_df) > 0:
        correct_answer_index = answer_df.index[0]
        df.at[correct_answer_index, 'guessed'] = 1
        print_state(df, answer_state)

    if answer_state == 'Quit' or correct_guesses == 50:
        game_on = False
        break

    screen.update()



screen.exitonclick()