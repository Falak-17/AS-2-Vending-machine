#VENDING MACHINE
#nested dictionary for items
import colorama 
from colorama import Fore 
colorama.init(autoreset=True)
print( Fore.GREEN + """ 
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

████████╗░█████╗░░██████╗████████╗██╗░░░██╗  ████████╗███████╗░█████╗░██╗░░██╗
╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝  ╚══██╔══╝██╔════╝██╔══██╗██║░░██║
░░░██║░░░███████║╚█████╗░░░░██║░░░░╚████╔╝░  ░░░██║░░░█████╗░░██║░░╚═╝███████║
░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░  ░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
░░░██║░░░██║░░██║██████╔╝░░░██║░░░░░░██║░░░  ░░░██║░░░███████╗╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░""")

input("Press any key to display the menu...")

stock = {Fore.CYAN +
    """
█▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀
▄█ █░▀█ █▀█ █▄▄ █░█ ▄█""": {
        1: {"Salted Chips": {"price": 1.50, "stock": 5,"calories": 156}},
        2: {"Cheddar Cheese":{"price": 1.75, "stock": 0,"calories": 130}},
        3: {"Chocolate Chip Cookies":{"price": 2.50, "stock": 4,"calories": 488}},
        4: {"Snickers":{"price": 1.25, "stock": 5,"calories":490}},
        5: {"Kitkat":{"price": 1.50, "stock": 7,"calories":490}},
        6: {"Ferrero Rocher":{"price": 4.50, "stock": 1,"calories":520}}},
Fore.CYAN +  """
█▀▄ █▀█ █ █▄░█ █▄▀ █▀
█▄▀ █▀▄ █ █░▀█ █░█ ▄█""":{
        7: {"Pepsi":{"price": 2.00, "stock": 5,"calories":155}},
        8: {"Sprite":{"price": 2.00, "stock": 2,"calories":155}},
        9: {"Bottled water":{"price": 1.00, "stock": 4,"calories":0}},
        10: {"Tea":{"price": 1.00, "stock": 2, "calories": 90}},
        11: {"Coffee":{"price": 3.00, "stock": 0, "calories": 130}},
        12: {"Orange juice":{"price": 1.75, "stock": 0,"calories":248}},
        13: {"Apple juice":{"price": 1.75, "stock": 3,"calories":248}}},
Fore.CYAN +   """
█▀▄ █▀▀ █▀ █▀ █▀▀ █▀█ ▀█▀
█▄▀ ██▄ ▄█ ▄█ ██▄ █▀▄ ░█░""": {
        14: {"Chocolate Icecream":{"price": 3.00, "stock": 5,"calories":170}},
        15: {"Strawberry Icecream":{"price": 3.00, "stock": 0,"calories":170}},
        16: {"Chocolate cake":{"price": 5.00, "stock": 3,"calories":371}},
        17: {"Strawberry Cheesecake":{"price": 7.50, "stock": 1,"calories":237}},
        18: {"Sprinkle Donut":{"price": 3.50, "stock": 7,"calories":220}},
        19: {"Chocolate Donut":{"price": 3.75, "stock": 5,"calories":240}}}}

def display_category(category_name, category_items):
    print(f"\n{category_name}:")                                                                                           #display category name
    print(f"{'No.':<5}{'Item':<25}{'Price(AED)':>10}{'Stock':>10}{'calories':>10}")                                        #header with coulmn names
    print("--------------------------------------------------------------")
    for item_num, item_details in category_items.items():                                              
        for item_name, details in item_details.items():
            print(f"{item_num:<5}{item_name:<25}{details['price']:>10.2f}{details['stock']:>10}{details['calories']:>10}") #display each categories items

def display_all_items():
    for category_name, category_items in stock.items():
        display_category(category_name, category_items)

import random

def choose_random_item():
    random_category=random.choice(list(stock.values()))                                                                    #select a random category from the stock
    random_item=random.choice(list(random_category.values()))                                                              #select a random item from the chosen category
    suggested_item_name=list(random_item.keys())[0]                                                                        #extract random item 
    item_details=random_item[suggested_item_name]                                                                          #extract item details
    return suggested_item_name, item_details                                                                               #Return the item and its details
    
def buy_product():
    total=0.0
    total_calories=0
    cart=[]                                                                                                                #initialize empty list
    while True:
        display_all_items()
        try:
            item_num=int(input("\nEnter the index number of the item you want to buy: "))                                  #input index number of desired item
            for category, items in stock.items():                                                                          #loop through each category and its corresponding items in the dictionary
                if item_num in items: 
                    category=category
                    item_details=list(items[item_num].values())[0]
                    item_name=list(items[item_num].keys())[0]
                    break
            if item_num>=20:
                print("Invalid product number. Please choose a valid product number.")                                     #invalid input
                continue
            if item_details["stock"]>0:                                                                                    #check stock
                quantity=int(input(f"Quantity of {item_name}: "))                                                          #input amount of item to be purchased
                if quantity<=item_details["stock"]:
                    total_price=item_details["price"]*quantity                                                             #multiply price with its quantity
                    total_calories+=item_details["calories"]*quantity                                                      #add calories based on quantity
                    total+=total_price                                                                                     #add to total price
                    item_details["stock"]-=quantity                                                                        #reduce stock
                    cart.append((item_name, quantity, total_price, item_details["calories"]*quantity))                     #append item details to the cart
                    suggested_item_name, suggested_item_details=choose_random_item()
                    print(f"With {item_name}, we would recommend {suggested_item_name}? ")                                  #display suggested item
                    print(f"Details: {suggested_item_details}")                                                            #display details of suggested item
                    response = input("Would you like to buy this suggested item? (y/n): ").lower()
                    if response == "y":
                        suggested_quantity = int(input(f"Quantity of {suggested_item_name}: "))
                        if suggested_quantity <= suggested_item_details["stock"]:
                            suggested_total_price = suggested_item_details["price"] * suggested_quantity
                            suggested_total_calories = suggested_item_details["calories"] * suggested_quantity
                            total += suggested_total_price
                            total_calories += suggested_total_calories
                            suggested_item_details["stock"] -= suggested_quantity
                            cart.append((suggested_item_name, suggested_quantity, suggested_total_price, suggested_total_calories))
                        else:
                            print(f"Sorry, only {suggested_item_details['stock']} {suggested_item_name} available.")
                else:
                    print(f"Sorry, only {item_details['stock']} {item_name} available.")                                   #available stock message
            else:
                print(f"Sorry, {item_name} is out of stock.")                                                              #out of stock message

            buy_more = input("\nDo you want to buy something else (y/n)? ").lower()                                        #Prompt to buy more items
            if buy_more!="y":                                                                                              #proceed for payment
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")                                                           #invalid input message
    payment(cart, total, total_calories)


def payment(cart, total, total_calories):
    print(Fore.GREEN + "\n𝓨𝓸𝓾𝓻 𝓬𝓪𝓻𝓽:")
    for item, quantity, price, calories in cart:                                                                           #display cart
        print(f"{quantity} x {item} = {price:.2f} AED ({calories} calories)")                                              #all items displayed with their prices and calories
    print(f"\nTotal amount: {total:.2f} AED")                                                                              #total amount
    print(f"Total calories: {total_calories} kcal")                                                                        #display total calories
    print("___________________________________________")
    payment_method = input("CHOOSE PAYMENT METHOD:\n1. Cash\n2. Card\nEnter the number: ")                                 #payment method
    if payment_method=="1":                                                                                                #cash payment
        print("\nYOU CHOSE CASH PAYMENT")
        while True:
            print(f"\nTotal amount: {total:.2f} AED")
            try:
                amount=float(input("Enter the amount you are paying: "))                                                   #input amount to pay
                if amount<total:                                                                                           #check if amount sufficient to total price
                    print("Insufficient amount. Try again.")                                                               #insufficient amount message
                else:
                    change=amount-total                                                                                    #calculate for change
                    print(f"Take your change: {change:.2f} AED")                                                           #returns change
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")                                                       #invalid amount message
    elif payment_method=="2":                                                                                              #card payment
        print("\nYOU CHOSE CARD PAYMENT")
        print("Swipe your card...")
    else:
        print("Invalid payment method. Please try again.")
    
    print(Fore.GREEN +"""\n\n                                                                                   
▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ █░█ 　 ▒█░░▒█ █▀▀█ █░░█ 
░▒█░░ █▀▀█ █▄▄█ █░░█ █▀▄ 　 ▒█▄▄▄█ █░░█ █░░█ 
░▒█░░ ▀░░▀ ▀░░▀ ▀░░▀ ▀░▀ 　 ░░▒█░░ ▀▀▀▀ ░▀▀▀""")                                                                           #dislpay final message

#main function
buy_product()