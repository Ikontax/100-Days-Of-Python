from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
make_coffee = CoffeeMaker()
bill = MoneyMachine()


coffee_machine = True


while coffee_machine:
    order_name = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if order_name == "report":
        make_coffee.report()
        bill.report()
    elif order_name == "quit":
        coffee_machine = False
    else:
        orderd_drink = coffee_menu.find_drink(order_name)

        if orderd_drink != None:
            if make_coffee.is_resource_sufficient(orderd_drink):
                if bill.make_payment(orderd_drink.cost):
                    make_coffee.make_coffee(orderd_drink)




