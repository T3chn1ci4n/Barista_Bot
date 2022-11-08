# Programing a Bot to say "Hello" and to be a Barista.

# NOTE ; This Barista Bot isn't taking anyone's job and not yours.....

# This will say welcome to the coffee shop and will ask for the user for him/her name.
print("Hello there, welcome to Dylaucino's Coffee shop.\n")

name = input("What is your name?\n")
# ! These are special EASTER EGGS that I have implemented into my barista bot when the user inputs a certain name.

if name == "Dylan":
    print("Oh, hey Boss! We hope you are having a great day today!")
    
# Names that are not part of the easter egg will be print a simple hello [NAME] and a welcome.
else:
    print(f"Hello {name}. We are glad that you come to order today!\n")
# This will ask the user or the customer for what type of coffee they would like in a loop. If the coffee does not exist then will rewind back to the same question and if the coffee does exist, then it will break the loop.
menu = "Black_Coffee ($1.5)\nEspresso ($1.0)\nLatte ($2.0)\nCappuccino ($2.5)\n"

while True:
    coffee =input(f"{name}, We have a range of coffees to order including sizes, here is the menu\n\nWe have got\n {menu}")

    if coffee == "Black_Coffee":
        coffeeCost = 1.5
        break
    elif coffee == "Espresso":
        coffeeCost = 1.0
        break
    elif coffee == "Latte":
        coffeeCost = 2.0
        break
    elif coffee == "Cappuccino":
        coffeeCost = 2.5
        break
    else:
        print("Sorry, We don't have that. \nPlease select one of the coffees above.")
        
# This while true loop will ask for a size cup for the coffee to break the loop. It will prompt the user to please choose the sides above if they choose something like extra small for example.
while True:

    size = input("And what size do you want out of Small ($1.0), Medium ($1.5) or Large? ($2.0) \n")
    
    if size == "Small":
        sizeCost = 1.0
        break
    elif size == "Medium":
        sizeCost = 1.5
        break
    elif size == "Large":
        sizeCost = 2.0
        break
    else:
        print("Please Choose the sizes above.")

# This line of code is a no brainer but it will ask how many cups does the user want.
while True:

    amount = input("And how many do you want?\n")
    
# The line of code below, will do the calculations and ask for the payment of the order.
    total = float(coffeeCost) + float(sizeCost)  *  float(amount)

    transaction = input("Thank you, that will be " + "$" +  str(total) + " please.\n$")

    paid = float(transaction) - float(total)
# These conditional statements will see if the payment is equal or greater than the cost of the order. If the payments is less than the cost f the order than it will reject the payment and start to ask the payment again. if the payment id greater however, then the barista bot will give back some changes
    if float(amount) > float(1.0):
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee}s and your ${paid} of changes.\n")
            break

        elif float(transaction) < float(total):
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")

        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}.\n")
            break

        else:
            False
    elif float(amount) == float(1.0):
        if float(transaction) > float(total):
            print(f"Here is your {amount} {size} {coffee} and your ${paid} of changes.\n")
            break

        elif float(transaction) < float(total):
            print(f"Sorry, You need ${total} to be able to pay the {amount} {size} {coffee}s.\n")


        elif float(transaction) == float(total):
            print(f"Here is your {amount} {size} {coffee}.\n")
            break

        else:
            False

    else:
        False
print("Thank you for ordering at Dylaucino's Coffee shop and have a nice day\n")