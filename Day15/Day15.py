"""
Day 15: Coffee Machine Program (Pt I)
"""
from initial_conditions import *


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


def update_resources(drink):
    """
    Removes the resources used to make the ordered drink
    :param drink: 'espresso', 'latte' or 'cappuccino'
    """
    for ingredient in ingredient_list:
        resources[ingredient] -= menu[drink]['ingredients'][ingredient]
    resources['money'] += menu[drink]['cost']


# Set initial conditions
menu = MENU
drink_list = [k for k in menu.keys()]
ingredient_list = [k for k in resources.keys()]
resources['money'] = 0
menu['espresso']['ingredients']['milk'] = 0
powered_on = True

# Continues operating until turned off
while powered_on:
    # Take order from customer
    order = input('What would you like? (espresso/latte/cappuccino) 🤔: ').lower()

    # Turns off machine
    if order == 'off':
        powered_on = False

    # Prints report or resource status
    if order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(resources['money'], 2)}")

    # Checks that input is valid
    if order in drink_list:

        # Checks that there are enough resources
        if enough_resources(order):
            # Requests payment
            print(f"That will be ${menu[order]['cost']:.2f} 🪙.")
            coins = insert_coins()
            change = round(coins - menu[order]['cost'], 2)

            # Checks that enough money was inserted
            if change >= 0:
                # Processes order
                update_resources(order)
                print(f'Here is your {order} ☕. Enjoy! Your change is ${change:.2f}.')

            else:
                print(f'Sorry that\'s not enough money. ${coins:.2f} refunded 🪙.')

    elif order == 'coffee':
        print('Plain coffee? That\'s too basic for this fancy-pants machine!')

    elif order == 'off':
        print('Powered off.')

    else:
        print('Invalid input.')








