print ("...WELCOME TO PASSWORD GENERATOR GAME...\n")
print("===password generater===\n")
import string
character = "abcdefghijklmnoppqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
length = int (input("enter your number : "))
import random
password = "".join(random.choice(character)for _ in range(length))
print ("\nyour generated password is : ",password)

