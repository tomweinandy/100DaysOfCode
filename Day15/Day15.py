"""
Day 15: Coffee Machine Program
"""

from initial_conditions import *

# Set initial conditions
menu = MENU
drink_list = [k for k in menu.keys()]
ingredient_list = [k for k in resources.keys()]
resources['money'] = 0
menu['espresso']['ingredients']['milk'] = 0


# Take order from customer
# order = input('What would you like? (espresso/latte/cappacino): ')
#
# if order == 'report':
#     print(f"Water: {resources['water']}ml")
#     print(f"Milk: {resources['milk']}ml")
#     print(f"Coffee: {resources['coffee']}g")
#     print(f"Money: ${round(resources['money'], 2)}")


def enough_resources(drink):
    """
    Checks if there is enough resources to fulfill a given order
    :param drink: 'espresso', 'latte' or 'cappucino'
    :return: True if enough ingredients to make the drink; otherwise, False
    """
    enough = True
    for ingredient in ingredient_list:
        if menu[drink]['ingredients'][ingredient] <= resources[ingredient]:
            pass
        else:
            print(f'Sorry there is not enough {ingredient}.')
            enough = False

    return enough


def insert_coins()
    coin_list = []

    while
    quarters = int()

order = drink_list[0]

if order in drink_list:
    if enough_resources(order):






