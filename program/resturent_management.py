menu = {
    'pizza': 120,
    'barger': 40,
    "coffie": 60,
    'saled': 70,
    'tea': 20
}
print("###__WELCOME TO PYTHON RESTURENT__###")
print("pizza: Rs 120\nbarger: RS 40\ncoffie: Rs 60\nsaled: Rs 70\ntea: Rs 20")
total_item = 0
item_1 = input("Enter your item that you want to order : ")
if item_1 in menu:
    total_item += menu[item_1]
    print(f"your item {item_1} is added.")
else:
    print(f"ordered item {item_1} is not available.")

another_item = input("Do you want to add another item? (yes/NO): ")
if another_item == "yes":
    item_2 = input("Enter your second order do you want : ")
    if item_2 in menu:
        total_item += menu[item_2]
        print(f"your item {item_2} is added.")
    else:
        print(f"item secons {item_2} is not available.")

print(f"The total amount item to pay is : {total_item}")        