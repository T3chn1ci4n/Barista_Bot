# Programing a Bot to say "Hello" and to be a Barista.
from datetime import datetime
import pyjokes

# NOTE ; This Barista Bot isn't taking anyone's job and not yours.....

# This will say welcome to the coffee shop and will ask for the user for their name.
print("Hello there, welcome to Dylaucino's Coffee shop.\n")

name = input("What is your name?\n")

# Names that are not part of the easter egg will be print a simple hello [NAME] and a welcome.
print(f"Hello {name}. We are glad that you come to order today!\n")

# This will ask the user or the customer for what type of service they would like in a loop.
# If the service does not exist then will rewind back to the same question. 
# If the service does exist, then it will break the loop.
menu = "Black_Coffee ($1.5)\nEspresso ($1.0)\nLatte ($2.0)\nCappuccino ($2.5)\nAmericano ($2.3)\nDoppio($3.0)\nFlat_White ($3.5)\n"
while True:
    selection = input(f"What services would you like {name}. J for [Joke], C for [Coffee], T for [Time] and Q for [Quit] ")
    selection = selection.lower()

    if selection in ["j", "joke"]:
        My_joke = pyjokes.get_joke(language="en", category="all")
        print(f"{My_joke}\n")

    elif selection in ["c", "coffee"]:
        break

    elif  selection in ["t", "time"]:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"The current time is {current_time}\n")
        
    elif selection in ["q", "quit"]: 
        quit("\nThank you for choosing us to serve you!")
    else:
        print("Please select options that are available!\n")   
# If the coffee service is selected, prompts the user to choose a coffee type. 
while True:
    coffee = input(f"\n{name}, We have a range of coffees to order including sizes, here is the menu\n\nWe have got\n{menu}")
    coffee = coffee.lower()
    if coffee in ["black"]:
        coffeeCost = 1.5
        break
    elif coffee in ["espresso"]:
        coffeeCost = 1.0
        break
    elif coffee in ["latte"]:
        coffeeCost = 2.0
        break
    elif coffee in ["cappuccino"]:
        coffeeCost = 2.5
        break
    elif coffee in ["americano"]:
        coffeeCost = 2.3
        break
    elif coffee in ["doppio"]:
        coffeeCost = 3
        break
    elif coffee in ["flat_white"]:
        coffeeCost = 3.5
        break

    else:
        print("Sorry, We don't have that. \nPlease select one of the coffees above.\n")

# This while true loop will ask for a size cup for the coffee to break the loop.
# It will prompt the user to please choose the sides above if they choose something like extra small for example.
while True:

    size = input("And what size do you want out of Small ($1.0), Medium ($1.5) or Large? ($2.0)\n")
    size = size.lower()

    if size in ["small"]:
        sizeCost = 1.0
        break
    elif size in ["medium"]:
        sizeCost = 1.5
        break
    elif size in ["large"]:
        sizeCost = 2.0
        break
    else:
        print("Please Choose the sizes above.\n")

while True:

    amount = input("And how many do you want?\n")

    if amount.isdigit():
        break
    else:
        print("Please choose a number!\n")

total = float(coffeeCost) + float(sizeCost)  *  float(amount)
# This line of code is a no brainer but it will ask how many cups does the user want.
while True:
    
# The line of code below, will do the calculations
# Prompts for the payment of the order.
    

    transaction = input("Thank you, that will be " + "$" +  str(total) + " please.\n$")

    paid = float(transaction) - float(total)
# These conditional statements will see if the payment is equal or greater than the cost of the order.
# If the payments is less than the cost f the order than it will reject the payment 
# Start to ask the payment again. if the payment id greater however, then the barista bot will give back some changes
    if float(amount) > float(1.0):
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee}s and your ${paid} of changes.\n")
            break

        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}.\n")
            break

        else:
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")

    elif float(amount) == float(1.0):
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee} and your ${paid} of changes.\n")
            break

        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}.\n")
            break

        else:
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")

    else:
        print()
print("Thank you for ordering at Dylaucino's Coffee shop and have a nice day\n")
