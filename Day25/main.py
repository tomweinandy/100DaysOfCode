"""
Day 25: U.S. States Game
"""
import turtle
import pandas as pd


def print_state(data, state):
    """
    Write correct guesses to the map
    :param data: dataframe of U.S. states
    :param state: the guessed state
    """
    answer_data = data[data['state'] == state]
    answer_idx = answer_data.index[0]
    x = answer_data['x'][answer_idx]
    y = answer_data['y'][answer_idx]

    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.write(state)
    t.goto(1000, 1000)


# Initialize screen, adding title and map
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# Add state data, including new column where correct guesses will be added
df = pd.read_csv('50_states.csv')
df['guessed'] = 0

# While game is True, let the player make a quess
game_on = True
while game_on:
    screen.update()

    # Show remaining states to guess as the title of the input box
    correct_guesses = sum(df['guessed'])
    title_str = f'{correct_guesses}/50 States Correct'

    # Take input, making lowercase then making titlecase
    answer_state = screen.textinput(title=title_str, prompt='What\'s another state\'s name?')
    answer_state = answer_state.lower().title()

    # Filter dataframe to only include row with guessed state (returns 0 rows if guessed state does not exist)
    answer_df = df[df['state'] == answer_state]

    # If guess matches a state (otherwise answer_df is empty with length 0)
    if len(answer_df) > 0:
        correct_answer_index = answer_df.index[0]
        df.at[correct_answer_index, 'guessed'] = 1
        print_state(df, answer_state)
        print(f'{answer_state} is a match!')
    elif answer_state == 'Exit':
        print('Saving list of remaining states to csv')
    else:
        print(f'"{answer_state}" does not exist (check your spelling)')

    # End game when player guesses all 50 states
    if correct_guesses == 50:
        game_on = False
        break

    # End game when player types 'exit' and save list of states to learn
    if answer_state == 'Exit':
        states_to_learn = df[df['guessed']==0]['state']
        states_to_learn = states_to_learn.reset_index(drop=True)
        states_to_learn.to_csv('states_to_learn.csv')

        game_on = False
        break

    screen.update()

screen.exitonclick()
