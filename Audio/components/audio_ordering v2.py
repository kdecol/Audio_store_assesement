#list of names of audio products
audio_names = ['Sony 12inch subs','Car amp','Sony tweeters','JBL tweeters','JBL single 10inch sub','AUX cord','Pioneer head unit','Double din Sony head unit',
               'Bluetooth audio adapter','Sub install kit','FM transmitter','Quad channel amp']

#list of audio product prices
audio_prices = [300, 150, 85, 60, 175, 22.50, 425, 465, 30.50, 69.99, 37.70, 230]

#list to store ordered audio products
order_list = []
#list to store audio product prices
order_cost = []


def menu():
    number_audio = 12
    for count in range (number_audio):
        print("{} {} ${:.2f}"   .format(count+1, audio_names[count],audio_prices[count]))

menu()


#ask for how many audio products they would like to order
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




#choose audio products from menu
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
        order_list.append(audio_prices[audio_ordered])
        print("{} ${:.2f}" .format(audio_names[audio_ordered],audio_prices[audio_ordered]))
        num_audio = num_audio-1
        

