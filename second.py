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

#get the possition ot the charecter
my_num = "Hellow worid" 
print(my_num[2:5])   

#we will print 1 to 10 number
for i in range (1,11):
    print(i)

# print a upper case letter and lower case letter
a = "Helow world"
print(a.upper())
b = "HELLOW WORLD"
print(b.lower())

# replace  the string
b = "Hello Rohit"
print(b.replace("R","M"))

# we will using of f string combine string and number each other
age = 32
txt = (f"my name is nitin kumar I ame  {age} year old") 
print(txt)

# display tyhe prise with decimal from
prise = 50
ptx = f"the prise is {prise:.2f}"
print(ptx)

#print yes if the function return true otherwise NO
def myfunction():
    return True
if myfunction():
    print("yes")
else:
    print("no")

# print item in list position 2 to position 6
list = ["apple","banana","papaya","lichi","pineapple","stobari","aanar"]   
print(list[1:6]) 

#change the value of a specfic item
thislist = ["apple","banana","papaya","lichi","pineapple","stobari","aanar"]
thislist [1] = "coconut"
print(thislist)

# using of insert method
list = ["apple","banana","cherry"]
list.insert(0,"orange")
print(list)

#  use the clear method.
list = ["apple","banana","cherry"]
list.clear()
print(list)

# we will print only thos item in which available "a"
thislist = ["apple","banana","cherry"]
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)

# take output in assending order using of short() method

this_list = ["apple","banana","mthis_listango", "kiwi","cherry"]
this_list.sort()
print(this_list)

# take output in desending order
this_list = ["apple","banana","mthis_listango", "kiwi","cherry"]
this_list.sort(reverse=True)
print(this_list)