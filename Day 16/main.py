from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from credentials import Authentication
import art

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
auth = Authentication()

while True:
    print(art.coffee)
    options = menu.get_items()
    choice = input(f"Which drink would you like to order? ({options}): ").lower()

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'exit' or choice == 'off':
        if auth.authenticate():
            exit()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)