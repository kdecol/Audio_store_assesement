# Audio bot program


import random
from random import randint

# List of names
names = ["Mark", "Allen", "kade", "Sean", "Luka", "Jayden", "Mk", "Daniel", "Joshua" "Holly"]
# Customer details dictionary

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

# Menu for click and collect or delivery

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