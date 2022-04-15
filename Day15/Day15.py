"""
Day 15: Coffee Machine Program
"""

from initial_conditions import *

# Set initial conditions
menu = MENU
drink_list = [k for k in menu.keys()]
ingredient_list = [k for k in resources.keys()]
# coin_list = [k for k in coins.keys()]

resources['money'] = 0
menu['espresso']['ingredients']['milk'] = 0


def enough_resources(drink):
    """
    Checks if there is enough resources to fulfill a given order
    :param drink: 'espresso', 'latte' or 'cappuccino'
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


def insert_coins():
    """
    Prompts the user to insert coins
    :return: total money added
    """
    quarters = ''
    dimes = ''
    nickles = ''
    pennies = ''

    # Forces correct input
    while type(quarters) != int:
        try:
            quarters = abs(int(input('How many quarters are you inserting?: ')))
        except:
            pass
    while type(dimes) != int:
        try:
            dimes = abs(int(input('How many dimes are you inserting?: ')))
        except:
            pass
    while type(nickles) != int:
        try:
            nickles = abs(int(input('How many nickles are you inserting?: ')))
        except:
            pass
    while type(pennies) != int:
        try:
            pennies = abs(int(input('How many pennies are you inserting?: ')))
        except:
            pass

    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total


# Take order from customer
order = input('What would you like? (espresso/latte/cappuccino): ')

if order == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(resources['money'], 2)}")


if order in drink_list:
    if enough_resources(order):
        print(f"That will be ${menu[order]['cost']:.2f}.")
        coins = insert_coins()
        change = round(coins - menu[order]['cost'], 2)
        if change >= 0:
            # update_resources(order)
            print(f'Here is your {order}. Enjoy! Your change is ${change:.2f}.')
        else:
            print(f'Sorry that\'s not enough money. ${coins:.2f} refunded.')






