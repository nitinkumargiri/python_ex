# # Student Marks System
# students = {}

# def add_student():
#     name = input("Enter name: ")
#     marks = float(input("Enter marks: "))
#     students[name] = marks
#     print(f"Added {name} with {marks} marks")

# def view_students():
#     for name, marks in students.items():
#         print(f"{name}: {marks}")

# def check_result(name):
#     if name in students:
#         marks = students[name]
#         if marks >= 35:
#             print(f"{name} passed with {marks} marks")
#         else:
#             print(f"{name} failed with {marks} marks")
#     else:
#         print("Student not found")

# # Main loop
# while True:
#     print("\n1. Add student\n2. View students\n3. Check result\n4. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         view_students()
#     elif choice == "3":
#         name = input("Enter name: ")
#         check_result(name)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice")
    
student = {}
def add_student():
    name = input("enter your name: ")
    mark = float(input("enter your mark: "))
    student[name] = mark
    print(f"student {name} with {mark} marks")
    
def view_student():
        for name ,mark in student.items():
            print(f('{name}: {mark}')) 

def cheak_result(name):
                if name in student:
                    mark = student[name]
                    if mark >= 35:
                        print(f"{name} passed with {mark} marks")
                    else:
                        print (f"{name} failed with {mark} marks") 
while True:
      print("\n1.add student\n2.view student\n3.check result\n4.exit")
      choice = input("enter your choice: ")
      if choice == "1":
          add_student()
      elif choice == "2":
          view_student()
      elif choice == "3":
          name = input("enter student name: ")
          cheak_result(name)
      elif choice == "4":
          break
      else:
          print("invalid choice")