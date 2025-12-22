menu = {
    'pizza': 120,
    'barger': 40,
    "coffie": 60,
    'saled': 70,
    'tea': 20,
    'paratha': 80,
    'veg': 150,
    'non-veg':180,
    'nudals': 50,
    'milk': 30,
    'jush': 50
}
print("####__WELCOME TO OUR PYTHON RESTURENT__####\n")
print("owner :-__ नितिन गिरी__\n")
print("pizza: Rs 120\nbarger: RS 40\ncoffie: Rs 60\nsaled: Rs 70\ntea: Rs 20\n")
print("paratha: Rs 80\nveg: Rs 150\nnon-veg: Rs180\nnudals: Rs 50\nmilk: Rs 30\njush: Rs 50")
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