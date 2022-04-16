"""
Coffee Machine Program (Pt II)
- This replicates the
"""

from Day16_menu import Menu, MenuItem
from Day16_coffee_maker import CoffeeMaker
from Day16_money_machine import MoneyMachine

# latte = MenuItem(
#     name='latte',
#     cost=2.5,
#     water=200,
#     milk=150,
#     coffee=24
# )

# Initialize class objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Set initial conditions
# order = ''
menu_list = menu.get_items().split('/')[:-1]  # Separate drinks into list (removing last item, which is empty)
input_list = menu_list + ['report', 'off']  # Add additional functions to input
# # drink_list = [k for k in menu.keys()]
# ingredient_list = [k for k in resources.keys()]
# resources['money'] = 0
# menu['espresso']['ingredients']['milk'] = 0
powered_on = True


# Machine operates while powered on
while powered_on:

    order = input(f'What would you like? ({menu.get_items()}): ')

    # Ask again if order is invalid
    while order not in input_list:
        order = input(f'What would you like? ({menu.get_items()}): ')

    # Print available resources and money in the machine
    if order == 'report':
        coffee_maker.report()
        money_machine.report()

    elif order in menu_list:
        drink = menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(drink):

            if money_machine.make_payment(drink.cost):

                coffee_maker.make_coffee(drink)

        else:
            print('Sorry, insufficient ingredients.')






    elif order == 'off':
        powered_on = False





# # todo 7. Make Coffee.
#     a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#         E.g. report before purchasing latte: Water: 300ml
#             Milk: 200ml
#             Coffee: 100g
#             Money: $0
#         Report after purchasing latte:
#             Water: 100ml
#             Milk: 50ml
#             Coffee: 76g
#             Money: $2.5
#     b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
