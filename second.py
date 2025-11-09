print("hellow world")
# Generate random number between 1 to 10 in python
import random
print(random.randrange(1,10))
'''I am going to use globle variaable'''
x = "owesome"
def myfunction():
    x = "fantastic"
    print("this is "+ x)
myfunction()
print("this is "+ x) 

# To change the value of global variable inside the function by using global keyword
x = "owesome"
def myfunction():
    global x
    x = "fantastic"
    print("this is "+ x)
myfunction()    
print("this is "+ x)

#convert one type to another type 
x = 1 #int
y = 2.1  # float
z = 1j  # complex 
#convert int to float
a = float(x)
#convert float to int
b = int (y)
#complex no is not changeable
c = complex (z)
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

for x in "banana":
    print(x)
    print(len(x))

# I am going to cheak something available in string or not
tex = "my name is nitin kumar from bihar"
for bihar in tex:
    print("yes , bihar is here")