menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']
def welcome():
    print("Welcome to the Drive-Thru!")
    print("Here's our menu:")
    for item in menu:
        print(item)

def order(item_number):
    return menu[item_number - 1]

welcome()
order_number = int(input("Please enter your order (1-5): "))
print("You ordered:", order(order_number))