"""
Day 83: Tic Tac Toe Game
"""
from prettytable import PrettyTable, ALL

def print_board(tic_tac_toe_list: list):
    """
    :param tic_tac_toe_list: list of nine tic-tac-toe positions
    """
    table = PrettyTable()
    table.header = False
    table.hrules = ALL
    table.padding_width = 3

    table.add_row(tic_tac_toe_list[0:3])
    table.add_row(tic_tac_toe_list[3:6])
    table.add_row(tic_tac_toe_list[6:])
    print(table)



# Make a list of nine blank entries that will serve as the board
ttt = [' ']*9

tic_tac_toe_list = [' ']*9
tic_tac_toe_list[0] = 'X'
tic_tac_toe_list[4] = 'X'
tic_tac_toe_list[8] = 'X'
print(tic_tac_toe_list)


def add_emojis(player, winning_index, tic_tac_toe_list):
    if player == 'X':
        emoji = '🙅'
    else:
        emoji = '🙆'

    for idx in winning_index:
        tic_tac_toe_list[idx] = emoji

    return tic_tac_toe_list


def check_for_winner(tic_tac_toe_list):
    # Identify winning permutations
    list_of_winning_indices = [
        [0, 1, 2],  # any row
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # any column
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # any diagonal
        [2, 4, 6]
    ]

    # Check each player if they have a winning set
    for player in ['X', 'O']:
        for winning_index in list_of_winning_indices:
            if tic_tac_toe_list[winning_index[0]] == player and \
                tic_tac_toe_list[winning_index[1]] == player and \
                    tic_tac_toe_list[winning_index[2]] == player:

                # Convert winning set to emojis
                winning_list = add_emojis(player, winning_index, tic_tac_toe_list)

                # Print outcome
                print(f'{player} wins!')
                print_board(winning_list)




