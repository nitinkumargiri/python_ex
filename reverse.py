num1 = int (input("enter your number : "))
rev = 0
while(num1 > 0):
    rev = rev * 10 + num1 %10
    num1 = num1/10
    break
print("your reverse no is ",rev)
     