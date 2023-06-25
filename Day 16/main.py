MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


resources = {
    "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money": 0,
}

user_wants = input("What would you like? (espresso/latte/cappuccino): ")


def check_resources(drink):
    """function that checks if resources are enough"""
    if (
        resources["Water"] - MENU[drink]["ingredients"]["water"] < 0
        or resources["Coffee"] - MENU[drink]["ingredients"]["coffee"] < 0
    ):
        return False

    if (
        user_wants != "espresso"
        and resources["Milk"] - MENU[drink]["ingredients"]["milk"] < 0
    ):
        return False

    return True


def report():
    """function that prints the report"""
    if user_wants == "report":
        for (key, value) in resources.items():
            print(f"{key}: {value}")


def user_coins():
    """function that calculates the the users coins"""
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))


"""function for making the drink"""
