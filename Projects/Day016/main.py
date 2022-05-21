"""
Coffee Machine Program (Pt II)
- This replicates the program from Day 15 but uses a class structure approach
- Only this file was created by me--the rest came from course resources
- See the pdf of documentation for details
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Initialize class objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Set initial conditions
menu_list = menu.get_items().split('/')[:-1]  # Separate drinks into list (removing last item, which is empty)
input_list = menu_list + ['report', 'off']    # Add additional functions to input
powered_on = True                             # You can't make coffee if the machine is off, obviously


# Machine operates while powered on
while powered_on:

    # Place order
    order = input(f'What would you like? ({menu.get_items()}): ')

    # Ask again if order is invalid
    while order not in input_list:
        order = input(f'What would you like? ({menu.get_items()}): ')

    # Print available resources and money in the machine
    if order == 'report':
        coffee_maker.report()
        money_machine.report()

    # Check drink is on the menu
    elif order in menu_list:
        drink = menu.find_drink(order)

        # Check sufficient resouces
        if coffee_maker.is_resource_sufficient(drink):

            # Check payment is sufficient
            if money_machine.make_payment(drink.cost):

                # Make the coffee
                coffee_maker.make_coffee(drink)

        else:
            print('Sorry, insufficient ingredients.')

    elif order == 'off':
        powered_on = False
