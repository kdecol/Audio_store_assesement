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
                    pickup_info()
                    break

                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("that is not a valid number")
            print ("Please enter 1 or 2")

# Click and collect information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
        
    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print(customer_details)
# Delivery information - name, adress and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
        
    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])


# Choose total number of products 



# List of audio products
audio_names = ['Sony 12inch subs','Car amp','Sony tweeters','JBL tweeters','JBL single 10inch sub','AUX cord','Pioneer head unit','Double din Sony head unit',
               'Bluetooth audio adapter','Sub install kit','FM transmitter','Quad channel amp']

audio_prices = [300, 150, 85, 60, 175, 22.50, 425, 465, 30.50, 69.99, 37.70, 230]



#print("How many pizzas would you like to order? ")
#num_pizza = int(input())
def menu():
    number_audio = 12
    for count in range (number_audio):
        print("{} {} ${:.2f}"   .format(count+1, audio_names[count],audio_prices[count]))


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
    order_type()
    menu()
   

main()