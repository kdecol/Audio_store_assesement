# Audio bot program


import random
from random import randint

# List of names
names = ["Mark", "Allen", "kade", "Sean", "Luka", "Jayden", "Mk", "Daniel", "Joshua" "Holly"]
# Customer details dictionary
customer_details = {}
# list of audio product names
audio_names = ['Sony 12inch subs','Car amp','Sony tweeters','JBL tweeters','JBL single 10inch sub','AUX cord','Pioneer head unit','Double din Sony head unit',
               'Bluetooth audio adapter','Sub install kit','FM transmitter','Quad channel amp']
#list of audio product prices prices
audio_prices =  [300, 150, 85, 60, 175, 22, 425, 465, 30, 69, 37, 230]

#list to store audio products
order_list = []
#list to store audio product prices
order_cost = []

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
    del_pick = ""
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
                    del_pick = "pickup"
                    break

                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("that is not a valid number")
            print ("Please enter 1 or 2")
    return del_pick

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
#print("How many pizzas would you like to order? ")
#num_pizza = int(input())
def menu():
    number_audio = 12
    for count in range (number_audio):
        print("{} {} ${:.2f}"   .format(count+1, audio_names[count],audio_prices[count]))


def order_audio():
    #ask for how mnay they would like to order
    num_audio = 0
    print ("")
    print ("Due to shortage in stock there is a limit of 12 items available for you to order. If you select more than 5 items, shipping is free. Otherwise there is a $9.00 shipping fee")
    while True:
        try:
            num_audio = int(input("How many audio products would you like to order? "))
            if num_audio >= 1 and num_audio <= 12: 
                break
            else: 
                print("Your order must be between 1 and 12")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter a number inbetween 1 or 12")
    #choose audio product from menu
    #count down until all audio products are ordered
    for item in range(num_audio):
        while num_audio > 0:
            while True:
                try:
                    audio_ordered = int(input("Please choose your audio products by entering the number from the menu "))
                    if audio_ordered >= 1 and audio_ordered <= 12: 
                        break
                    else: 
                        print("Your order must be between 1 and 12")
                except ValueError:
                    print ("That is not a valid number")
                    print ("Please enter a number inbetween 1 or 12")
            audio_ordered = audio_ordered-1
            order_list.append(audio_names[audio_ordered])
            order_cost.append(audio_prices[audio_ordered])
            print("{} ${:.2f}" .format(audio_names[audio_ordered],audio_prices[audio_ordered]))
            num_audio = num_audio-1
        

# Order - from store list - print each product with cost
# Print order out - including if order is for delivery or click and collect and names and prices
def print_order(del_pick):
    total_cost = sum(order_cost) 
    print("Customer Details")
    if del_pick == "pick up":
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("your order is for Delivery")
        if len(order_list) < 6:
            total_cost = total_cost + 12
            print("You have ordered 5 or less items, a $12 delivery charge will incur")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"Total: ${total_cost}")


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
    del_pick = order_type()
    print(del_pick)
    menu()
    order_audio()
    print_order(del_pick)
   

main()