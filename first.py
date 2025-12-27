# print("hellow world")
# x = 100
# y = 822
# if (x > y):
#     print("hello world")
# else:
#     print("good bye..")

# # i will going to cheak that how many time repete no.
# thistuple = (2,3,4,5,6,7,8,5,4,5,45)
# x = thistuple.count(2)
# print(x)

# # convert a touple into a list
# thistuple = ("apple","banana","cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# #example the length of  dictionary
# thisdict = {"apple" : "banana" , "cherry" : 1964}
# print(len(thisdict))

# # print the type of the dictionary
# thisdict = {"papaya" : "graps" , "banana" : "apple"}
# print(type(thisdict))

# # using of set
# thisset = {"apple","banana","cherry"}
# thatset = {"mango","papaya","banana"}
# set3 = thisset.intersection(thatset)
# print(set3)
# dict = {"apple":"bamana","modle":"a1"}
# print(dict["modle"])

# thisdict = {"brandf":"tata","modle":"mahindra",
#             "year": 2000}
# x = thisdict
# print(x)
# x["year"] = 2020
# print(x)
# #using the update method
# this = {"modle":"car","year":2003}
# this.update({"year":2004})
# print(this)
# x = this
# x.update({"coler":"red"})
# print(x)
# #using of del keword
# del this["modle"]
# print(this)


dixt = {"name" : "nitin",
        "roll no":20241094,
          "age":18,}
print(len(dixt))
print(type(dixt))
user = input("enter your costumer info: ")
for user in dixt:
    print(dixt[user])

