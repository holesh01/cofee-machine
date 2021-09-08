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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
def report_print():
    print("Water=",resources["water"],"ml")
    print("Milk=", resources["milk"],"ml")
    print("Coffe=", resources["coffee"],"g")
    print("Money=", resources["money"],"$")

def insert_coin():
    quarters=int(input("how many quarters: "))
    dimes=int(input("how many dimes: "))
    nickles=int(input("how many nickles: "))
    pennis=int(input("how many pannies: "))

    return ((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennis*0.01))

# TODO: 1.print report
is_on=True
while(is_on):
    user_wish=input("What would you like? (espresso/latte/cappuccino):")

    if user_wish.lower()=="report":
        report_print()
    elif user_wish.lower()=="off":
        is_on=False
    elif user_wish.lower()=="espresso":
        if resources["water"]>=50 and resources["milk"]>=0 and resources["coffee"]>=18:
            ammount=insert_coin()
            if ammount >= 1.5:
                final_amm=round(ammount-1.5,2)
                print(f"Here is {final_amm} in change")
                print("Here is your espresso ☕.Enjoy!")
                resources["water"]-=50
                resources["milk"]-=0
                resources["coffee"]-=18
                resources["money"]+=1.5
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough ingredients.")
    elif user_wish.lower()=="latte":
        if resources["water"]>=200 and resources["milk"]>=150 and resources["coffee"]>=24:
            ammount=insert_coin()
            if ammount >= 2.5:
                final_amm=round(ammount-2.5,2)
                print(f"Here is {final_amm} in change")
                print("Here is your espresso ☕.Enjoy!")
                resources["water"]-=200
                resources["milk"]-=150
                resources["coffee"]-=24
                resources["money"]+=2.5
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough ingredients.")
    elif user_wish.lower()=="cappuccino":
        if resources["water"]>=250 and resources["milk"]>=100 and resources["coffee"]>=24:
            ammount=insert_coin()
            if ammount >= 3:
                final_amm=round(ammount-3,2)
                print(f"Here is {final_amm} in change")
                print("Here is your espresso ☕.Enjoy!")
                resources["water"]-=250
                resources["milk"]-=100
                resources["coffee"]-=24
                resources["money"]+=3
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough ingredients.")

    else:
        print("Wrong input!")