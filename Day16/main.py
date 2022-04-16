from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem(
    name='latte',
    cost=2.5,
    water=200,
    milk=150,
    coffee=24
)

menu = Menu([latte])

