print("hellow world")
x = 100
y = 822
if (x > y):
    print("hello world")
else:
    print("good bye..")

# i will going to cheak that how many time repete no.
thistuple = (2,3,4,5,6,7,8,5,4,5,45)
x = thistuple.count(2)
print(x)

# convert a touple into a list
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#example the length of  dictionary
thisdict = {"apple" : "banana" , "cherry" : 1964}
print(len(thisdict))

# print the type of the dictionary
thisdict = {"papaya" : "graps" , "banana" : "apple"}
print(type(thisdict))

# using of set
thisset = {"apple","banana","cherry"}
thatset = {"mango","papaya","banana"}
set3 = thisset.union(thatset)
print(set3)