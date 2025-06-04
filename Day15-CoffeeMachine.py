Money = 0
coffee = 300
milk = 200
water = 400

receipt = {
    "cappucino": {
        "water" : 250, 
        "coffee": 24,
        "milk": 100,
        "cost": 3.00
    },
        "latte": {
        "water" : 200, 
        "coffee": 24,
        "milk": 150,
        "cost": 2.50
    },
        "espresso": {
        "water" : 50, 
        "coffee": 18,
        "milk": 0,
        "cost": 1.50
    }
}

def coffeemachine(input1):
    notEnough = "Sorry there is not enough"
    global water, coffee, milk, receipt, Money
    if(water < receipt[input1]["water"]):
        notEnough += " water"
    if(coffee < receipt[input1]["coffee"]):
        notEnough += " coffee"
    if(milk < receipt[input1]["milk"] ):
        notEnough += "milk"
    if(notEnough != "Sorry there is not enough"):
        print(notEnough)
    else:
        print("Please intsert coins:")
        Quarters, Dimes, Nickles, Pennies = 0,0,0,0
        Quarters = int(input("How many Quarters?: "))
        Dimes = int(input("How many Dimes?: "))
        Nickles = int(input("How many Nickels?: "))
        Pennies = int(input("How many Pennies?: "))
        clientBalance = (Quarters * 0.25)+(Dimes * 0.10)+(Nickles * 0.5)+(Pennies * 0.01)
        if(clientBalance < receipt[input1]["cost"]):
            print("Sorry Thats not enough money. Money refunded.")
        else:
            Money += receipt[input1]["cost"]
            water -= receipt[input1]["water"]
            coffee -= receipt[input1]["coffee"]
            milk -= receipt[input1]["milk"]
            refund = clientBalance - receipt[input1]["cost"]
            if(refund != 0):
                print(f"Here is ${refund:.2f} in change")
            print("Here is your {input1} enjoy!") 

def main():
    while(1):
        input1 = input("What would you like? (espresso/latte/cappuccino): ")
        match input1:
            case "espresso":
                coffeemachine(input1)       
            case "latte":
                coffeemachine(input1)
            case "cappucino":
                coffeemachine(input1)
            case "report":
                print(f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}g\nMoney: ${Money:.2f}" )
            case "off":
                exit()
            case _:
                print("Sorry I didn't got your request. Please try again!")


main()