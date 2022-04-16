"""
Coffee Machine Program (Pt II)
- This replicates the
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# latte = MenuItem(
#     name='latte',
#     cost=2.5,
#     water=200,
#     milk=150,
#     coffee=24
# )

menu = Menu()

# Separate drinks into list (removing last item, which is empty)
menu_list = menu.get_items().split('/')[:-1]

# Force correct drink order from list
order = ''
while order not in menu_list:
    order = input(f'What would you like? ({menu.get_items()}): ')


print(menu_list)
