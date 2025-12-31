'''
grade = 'A'
excelent
grade = 'B'
good
grade = 'c'
pass
grade = 'D'
fail 

'''
hindi = int(input("enter your hindi result: "))
eng = int(input("enter your english result: "))
math = int(input("enter your math result: "))
science = int (input("enter your science result: "))
sst = int(input("enter your social science result:"))

total_mark = hindi + eng + math + science + sst
percentage = int(total_mark / 5)

if percentage >= 80:
    grade = 'A+'
elif percentage >= 70:
    grade = 'A'
elif percentage >= 60:
    grade = 'B+'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 30:
    grade = 'C'
else:
    grade = 'F'

print(f"your total mark is : {total_mark}")    
print(f"your percentage is : {percentage}%")
print("your grad is : ",grade)
