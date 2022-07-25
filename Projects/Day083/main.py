"""
Day 83: Tic Tac Toe Game
"""
from prettytable import PrettyTable, ALL


def print_board(tic_tac_toe_list: list):
    """
    Converts list of entries into a printed table
    :param tic_tac_toe_list: list of nine tic-tac-toe positions
    """
    # Define and format pretty table
    table = PrettyTable()
    table.header = False
    table.hrules = ALL
    table.padding_width = 3

    # Built table from list
    table.add_row(tic_tac_toe_list[0:3])
    table.add_row(tic_tac_toe_list[3:6])
    table.add_row(tic_tac_toe_list[6:])

    print(table)


def add_emojis(player, winning_index, tic_tac_toe_list):
    """
    Replaces the winning set of marks with emojis.
    :param player: The winning player
    :param winning_index: The list of three numbers that builds an index for a winning set.
    :param tic_tac_toe_list: List of entries.
    :return: The tic_tac_toe_list
    """
    if player == 'X':
        emoji = '🙅'
    else:
        emoji = '🙆'

    for idx in winning_index:
        tic_tac_toe_list[idx] = emoji

    return tic_tac_toe_list


def check_for_winner(tic_tac_toe_list):
    """
    Checks if there is a winner in the current game
    :param tic_tac_toe_list: list of entries
    :return: True/False whether we have a winner.
    """
    we_have_a_winner = False

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

                we_have_a_winner = True

                # Convert winning set to emojis
                winning_list = add_emojis(player, winning_index, tic_tac_toe_list)

                # Print outcome
                print_board(winning_list)
                print(f'{player} wins!')

    return we_have_a_winner


def check_for_draw(tic_tac_toe_list):
    """
    Checks if there is a draw in the current game
    :param tic_tac_toe_list: list of entries
    :return: True/False whether we have a draw.
    """
    if ' ' in tic_tac_toe_list:
        we_have_a_draw = False
    else:
        we_have_a_draw = True
        print_board(tic_tac_toe_list)
        print(f'No winner.\n')

    return we_have_a_draw


def change_active_player(active_player):
    """
    Changes active player
    :param active_player: Previous active player
    :return: New active player, opposite of previous
    """
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
while game_on:
    # Define current game state
    winner = False
    draw = False

    # Make a list of nine blank entries that will serve as the board
    ttt = [' '] * 9

    # Identify who goes first
    active_player = ''
    while active_player not in ['X', 'O']:
        active_player = input('Which player goes first? ("x" or "o"): ').upper()

    # Show instructions
    print_board(coordinates)
    print('Use the above cardinal directions to identify where to place your mark.')
    print_board(ttt)

    # Continue playing until there is a winner or draw
    while not winner and not draw:
        # Requires user to input valid square
        square = ''
        while square not in coordinates:
            square = input(f'Where does Player {active_player} want to go?: ').lower()

            # Cancel move if space is occupied
            idx = board_dict[square]
            if ttt[idx] != ' ':
                print(f'The {square.upper()} square is occupied. Try again.')
                square = ''
            else:
                ttt[idx] = active_player

        # See if there is a winner
        winner = check_for_winner(ttt)

        if not winner:
            # See if there is an empty square left
            draw = check_for_draw(ttt)

            if not draw:
                # Otherwise, let the next player go
                active_player = change_active_player(active_player)
                print_board(ttt)

    # Ask if player wants to play again
    play_again = ''
    while play_again not in ['y', 'n']:
        play_again = input('Play again? (y or n): ').lower()

    if play_again == 'n':
        game_on = False
        print('\nThanks for playing!\n')
