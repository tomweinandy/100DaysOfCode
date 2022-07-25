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

                # Turn off the game
                game_on = False

                # Convert winning set to emojis
                winning_list = add_emojis(player, winning_index, tic_tac_toe_list)

                # Print outcome
                print_board(winning_list)
                print(f'{player} wins!')

                break


def change_active_player(active_player):
    if active_player == 'X':
        new_active_player = 'O'
    else:
        new_active_player = 'X'
    return new_active_player


# Create dictionary of coordinates and indices
board_dict = {'nw': 0,
              'n': 1,
              'ne': 2,
              'w': 3,
              'c': 4,
              'e': 5,
              'sw': 6,
              's': 7,
              'se': 8}
coordinates = [key for key in board_dict.keys()]

# Begin game
game_on = True
winner = False

while game_on:
    # Make a list of nine blank entries that will serve as the board
    ttt = [' '] * 9

    # Identify who goes first
    active_player = ''
    while active_player not in ['X', 'O']:
        active_player = input('Which player goes first? ("x" or "o"): ').upper()

    # Show instructions
    print('\nUse the below cardinal directions to identify where to place your mark.')
    print_board(coordinates)

    print(f'\nPlayer {active_player} goes first.')
    print_board(ttt)

    # Continue playing until a winner is declared
    while not winner:
        square = ''
        while square not in coordinates:
            square = input(f'\nWhere does Player {active_player} want to go?: ').lower()

            # Cancel move if space is occupied
            idx = board_dict[square]
            if ttt[idx] != ' ':
                print(f'The {square.upper()} square is occupied. Try again.')
                square = ''
            else:
                ttt[idx] = active_player

        # See if there is a winner yet
        check_for_winner(ttt)

        if not game_on:
            # Otherwise, let the next player go
            active_player = change_active_player(active_player)
            print_board(ttt)

    game_on = False





