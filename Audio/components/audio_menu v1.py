audio_names = ['Sony 12inch subs','Car amp','Sony tweeters','JBL tweeters','JBL single 10inch sub','AUX cord','Pioneer head unit','Double din Sony head unit',
               'Bluetooth audio adapter','Sub install kit','FM transmitter','Quad channel amp']

audio_prices = [300, 150, 85, 60, 175, 22.50, 425, 465, 30.50, 69.99, 37.70, 230]



#print("How many pizzas would you like to order? ")
#num_pizza = int(input())
def menu():
    number_audio = 12
    for count in range (number_audio):
        print("{} {} ${:.2f}"   .format(count+1, audio_names[count],audio_prices[count]))

menu()