# import
print("....WELCOME TO ROCK PAPPER SCISOR GAME....\n\n")
print("chose: 1 = 'rock'..\nchose: 2 = 'paper'..\nchose: 3 = 'scissor..\n\n")

userchoice = int (input("enter your choice : "))
import random
computerchoice = (random.randrange(1,4))
print("enter computer choice : ",computerchoice)

# if(userchoice == computerchoice):
#     print("mach is draw....")
# elif((userchoice == 1 and computerchoice == 3) or (userchoice == 2 and computerchoice == 1)
#      or (userchoice == 3 and computerchoice == 2)):
#     print("you win....")
# else:
#     print("computer win...")

