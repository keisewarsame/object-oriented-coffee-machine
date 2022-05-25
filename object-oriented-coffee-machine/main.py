import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_1 = Menu()
# menu_item = MenuItem()
coffee_maker_1 = CoffeeMaker()
money_machine_1 = MoneyMachine()


is_on = True

while is_on:
    options = menu_1.get_items()
    choice = input(f"What would you like? ({options}) ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_1.report()
        money_machine_1.report()
    else:
        order = menu_1.find_drink(choice)
        if coffee_maker_1.is_resource_sufficient(order):
            if money_machine_1.make_payment(order.cost):
                coffee_maker_1.make_coffee(order)