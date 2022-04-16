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

    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    #
    elif order in menu_list:
        drink = menu.find_drink(order)
        print(coffee_maker.is_resource_sufficient(drink))

        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
            print(f'Here is your {drink.name}. Enjoy!')
        else:
            print('Sorry, insufficient ingredients.')






    elif order == 'off':
        powered_on = False



# # todo 5. Process coins.
#     a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#     b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#     c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#         pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# # todo 6. Check transaction successful?
#     a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
#     b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
#         Milk: 50ml
#         Coffee: 76g
#         Money: $2.5
#     c. If the user has inserted too much money, the machine should offer change.
#         E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
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
