#create an empty eliment
item = []

#take list input from 
n = int(input ("enter number of item you want to add in list: "))

#by using for loop storing no of list 
# {i + 1} use for counting in enter item in terminal like
'''
enter item 1:
enter item 2:
enter item 3:
'''
for i in range(n):
    value = input(f"enter item {i + 1}: ")
    item.append(value)

print("stored list: ",item)



# # create an empty list
# items = []

# # number of elements
# n = int(input("Enter number of items: "))

# # storing values in list
# for i in range(n):
#     value = input(f"Enter item {i + 1}: ")
#     items.append(value)

# # display the list
# print("Stored List:", items)

    