#Define the menu of restaurant
menu ={
    'pizza':100,
    'burger':80,
    'pasta':120,
    'salad':50,
    'coffee':80,
}
print("Welcome to the restaurant!")
print("here is the menu:")
print("pizza:Rs100\n burger:Rs80\npasta:Rs120\nsalad:Rs50\ncoffee:Rs80")
order_total=0
item_1=input("enter the item you want to order:")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order:")
else:
    print(f"sorry, we don't have {item_1} on the menu")

another_order=input ("do you want to order another item?(yes/no):")
if another_order=="yes":
    item_2=input("enter the item you want to order:")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item {item_2} has been added to your order:")
    else:
        print(f"sorry, we don't have {item_2} on the menu")

print("The total amount of your order is:", order_total)
print("Thank you for your order!")

print("enjoy your meal!")

