#list to store ordered audio products
order_list = ['Sony 12inch subs','Car amp','Sony tweeters','JBL tweeters']
#list to store audio product prices
order_cost = [300, 150, 85, 60]

customer_details = {'name':'kade', 'phone':'0212601495', 'house':'5', 'street':'Batkinj', 'suburb':'Papakura'}

#print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House: {} \nCustomer Street: {} \nCustomer Suburb: {}".format(  customer_details['name'],customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb']))

print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")


count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1