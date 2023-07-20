# Audio bot program


import random
from random import randint

# List of names
names = ["Mark", "Allen", "kade", "Sean", "Luka", "Jayden", "Mk", "Daniel", "Joshua" "Holly"]
# Customer details dictionary
customer_details = {}

# Welcome message with random names
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message 
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to KSC Audio")
    print("*** My name is", name, "***")
    print("***I will be here to help you order your dream audio setup***")

# Validates inputs to cheack if they are blank
def not_blank(question):
    valid = False
    while not valid:
        responce = input(question)
        if responce != "":
            return responce.title()
        else:
            print("This can not be blank")
            
# Menu for click and collect or delivery
def order_type():
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect please enter 1")
    print("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and collect")
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("that is not a valid number")
            print ("Please enter 1 or 2")

# Click and collect information - name and phone number

# Delivery information - name, adress and phone

# Choose total number of products 

# List of audio products

# Order - from store list - print each product with cost

# Print order out - including if order is for delivery or click and collect and names and prices

# Ability to cancel or proceed with order

# Options for new order or to exit

# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message 
    Parameters: None
    Returns: None
    '''
    welcome()

main()