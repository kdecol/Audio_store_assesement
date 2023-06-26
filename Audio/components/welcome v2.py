import random
from random import randint

#List of names
names = ["Mark", "Allen", "kade", "Sean", "Luka", "Jayden", "Mk", "Daniel", "Joshua" "Holly"]

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

def main():
    '''
    Purpose: To run all functions
    a welcome message 
    Parameters: None
    Returns: None
    '''
    welcome()

main()