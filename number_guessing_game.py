print("....WEELCOME TO NUMBER GUESSING GAME....\n")
print("   ..enter number between (1 - 100)..\n")
guess = int (input("enter your number : "))
import random
computerguess = random.randrange(1,100)
print("computer guess no is : ",computerguess)
if(guess < computerguess):
    print("number too low....")
elif(guess > computerguess):
    print("number too heigh...")
else:
    print("congratulation: your number is same\nits a lucky number..")