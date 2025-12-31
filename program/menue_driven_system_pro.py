
while True:
    num = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"The addition {num} + {num2} = {num + num2}")

    elif choice == 2:
        print(f"The subtraction {num} - {num2} = {num - num2}")

    elif choice == 3:
        print(f"The multiplication {num} * {num2} = {num * num2}")

    elif choice == 4:
        if num2 != 0:
            print(f"The division {num} / {num2} = {num / num2}")
        else:
            print("Error: Division by zero is not allowed")

    else:
        print("Invalid choice")

    ans = input("\nDo you want to continue (y/n): ")
    ans = ans.lower()
    if ans != 'y':
        break
