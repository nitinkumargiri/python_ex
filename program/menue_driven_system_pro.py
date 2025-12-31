while True:
    num = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    print("1.addition\n2. suubstraction\n3. multiplication\n4. division")

    choice = int(input("enter your choice: "))
    if choice == 1:
        print(f"the addition{num} + {num2} = ",num +num2)
    elif choice == 2:
        print(f"the substraction {num} - {num2} = ",num - num2)
    elif choice == 3:
        print(f"the multiplication {num} * {num2} = ",num * num2)
    elif choice == 4:
        print(f"the division {num} / {num2} = ",num / num2)
    else:
        print("invalid choice")
        ans = input("do you want to continue y/n: ")
        ans = ans.lower()
        if ans != 'y':
            break