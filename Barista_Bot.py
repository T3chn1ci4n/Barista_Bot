# program to create a barista bot for a coffee shop. 
# This Barista Bot is designed to make it easier for people with hearing disabilities to order at a café-like environment.
from datetime import datetime
from pyjokes import get_joke

# function to display the current time
def clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"The current time is {current_time}\n")


#  created a dictionary that maps names to responses.
print("Hello there, welcome to Dylaucino's Coffee shop.\n")

# ! These are special EASTER EGGS that I have implemented into my barista bot when the user inputs a certain name.
responses = {
    "Dylan": "Oh, hey Boss! We hope you are having a great day today! How is day going?",
}
# Getting the user's name and checking for the existance of the name in the dict
name = input("What is your name?\n")

# check if the name is a key in the dictionary, and if so, print the corresponding value
if name in responses:
    while True:
        print(responses[name])
        Q = input("\n").lower()
        # check the followup question here
        if Q in ["good", "g"]:
            print("\nThat is good!")
            break
        elif Q in ["bad", "b"]: 
            print("\nOh, Well hopefully things get better.")
            break
        else:
            print("Pardon, Not to be rude but you didn't answer my question?")
else:
    print(f"Hello, {name}, We are so glad you come to order today")


while True:
    # prompt user for service selection
    selection = input(f"What services would you like {name}. J for [Joke], C for [Coffee], T for [Time] and Q for [Quit] ")
    selection = selection.lower()

    # if the user selects 'joke', get a random joke
    if selection in ["j", "joke"]:
        My_joke = get_joke(language="en", category="all")
        print(f"{My_joke}\n")
    # if the user selects 'coffee', break out of the loop
    elif selection in ["c", "coffee"]:
        break

    elif selection in ["t", "time"]:
        clock()
        
    elif selection in ["q", "quit"]: 
        quit("\nThank you for choosing us to serve you!")
    else:
        print("Please select options that are available!\n") 

while True:
    menu = "Black ($1.5)\nEspresso ($1.0)\nLatte ($2.0)\nCappuccino ($2.5)\nAmericano ($2.3)\nDoppio($3.0)\nFlat_White ($3.5)\n"

    coffee = input(f"\n{name}, We have a range of coffees to order including sizes, here is the menu\n\nWe have got\n{menu}")
    coffee.lower()

    coffee_selection = {
    "black": 2,
    "latte": 2.5, 
    "flat_white": 3, 
    "espresso" : 2.5, 
    "cappuccino" : 2.5, 
    "americano" : 2.3, 
    "doppio" : 3}

    if coffee in coffee_selection:
        print(f"The price of a {coffee} is ${coffee_selection[coffee]}")
        yn = input("Will you like to continue with that order?\n")
        if yn in ["y", "yes"]: 
            coffeeCost = coffee_selection[coffee] 
            break
        elif yn in ["n", "no"]: continue

        else: 
            print("Please select if you like to continue with that order!\n")
    else:
        print("Sorry, We don't have that.\nPlease select one of the coffees above.\n")


while True:

    size = input("And what size do you want out of Small ($1.0), Medium ($1.5) or Large? ($2.0)\n")
    size = size.lower()

    size_selection = {
        "small" : 1,
        "medium" : 1.5,
        "large" : 2
    }

    if size in size_selection:
        print(f"The price of a {size} {coffee} is ${coffeeCost + size_selection[size]}")
        yn = input("Will you like to continue with that order?\n\n")
        if yn in ["y", "yes"]: 
            sizeCost = size_selection[size] 
            break
        elif yn in ["n", "no"]: continue
        else: 
            print("Please select if you like to continue with that order!\n")
    else:
        print("Please Choose the sizes above.\n")

while True:
    try:
        amount = int(input("And how many do you want?\n"))
        break
    except ValueError:
        print("Please choose a digital number!\n")

total = float(coffeeCost) + float(sizeCost)  *  float(amount)

while True:
    while True:
        transaction = input(f"Thank you, that will be ${total} please.\n$")
        try:
            float(transaction)
            paid = float(transaction) - float(total)
            break
        except ValueError:
            print("Please choose a number!\n")

# These conditional statements will see if the payment is equal or greater than the cost of the order. If the payments is less than the cost f the order than it will reject the payment and start to ask the payment again. if the payment id greater however, then the barista bot will give back some changes
    if float(amount) > float(1.0):
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee}s and your ${paid} of changes.\n")
            break

        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}s.\n")
            break

        else:
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")

    else:
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee} and your ${paid} of changes.\n")
            break

        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}.\n")
            break

        else:
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")

print("Thank you for ordering at Dylaucino's Coffee shop and have a nice day\n")
