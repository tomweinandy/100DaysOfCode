"""
Day 83: Tic Tac Toe Game
"""
from prettytable import PrettyTable, ALL
# 🙅🙆

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
print_board(ttt)


# Identify winning permutations

