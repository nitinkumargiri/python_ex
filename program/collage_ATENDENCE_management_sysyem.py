print ("welcome to collage attendence management system")
print ("author: nitin giri\n")
atendence = int(input("enter your atedence percentage: "))
if atendence >= 80:
    print("you are a eligible for a exam with better atendence score .")
elif atendence >= 75:
    print ("Good! you are eligible for exam")
elif atendence >= 65:
    print ("you are eligible for exam with bad percentage of atendance")
else:
    print("sorry! you are not eligible for exam due to low atendance percentage..")