

import numpy as np

student_info = {
    "Name" : [],
    "Math Grade" : [], 
    "Science Grade" : [],
    "English_Grade" : [],
    "Final_Grade" : [], 
    "Category" : [],
    "Status" : []
}

column = ""

def input_student_info():
    name = input("Enter student's name: ").strip()

    if not name:
        print("Invalid input. Name cannot be empty!")
        return

    if name.isdigit():
        print("Invalid input. Name cannot be a number!")
        return

    if name in student_info["Name"]:
        print("Student already exists!!")
        return

    student_info["Name"].append(name)
    student_info["Math Grade"].append("")
    student_info["Science Grade"].append("")
    student_info["English_Grade"].append("")
    student_info["Final_Grade"].append("")
    student_info["Category"].append("")
    student_info["Status"].append("")
    print("Student added successfully!!")


def add_grade():
    name = input("Enter student's name: ").strip()

    if not name:
        print("Invalid input. Name cannot be empty!")
        return

    if name not in student_info["Name"]:
        print("Student not found!!")
        return

    try:
        math_grade = float(input("Enter Math grade : "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the Math grade.")
        return

    try:
        science_grade = float(input("Enter Science grade : "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the Science grade.")
        return

    try:
        english_grade = float(input("Enter English grade : "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the English grade.")
        return

    if math_grade < 0 or math_grade > 100 or science_grade < 0 or science_grade > 100 or english_grade < 0 or english_grade > 100:
        print("Invalid input. Grades must be between 0 and 100.")
        return

    if math_grade >= 90 and science_grade >= 90 and english_grade >= 90:
        category = "A"
        status = "Passed"
    elif math_grade >= 80 and science_grade >= 80 and english_grade >= 80:
        category = "B"
        status = "Passed"
    elif math_grade >= 75 and science_grade >= 75 and english_grade >= 75:
        category = "C"
        status = "Passed"
    elif math_grade >= 60 and science_grade >= 60 and english_grade >= 60:
        category = "D"
        status = "Failed"
    else:
        category = "F"
        status = "Failed"

    final_grade = (math_grade + science_grade + english_grade) / 3
    index = student_info["Name"].index(name)

    student_info["Math Grade"][index] = math_grade
    student_info["Science Grade"][index] = science_grade
    student_info["English_Grade"][index] = english_grade
    student_info["Final_Grade"][index] = final_grade
    student_info["Category"][index] = category
    student_info["Status"][index] = status
    print("Grades added successfully!!")


def view_student_info():
    if not student_info["Name"]:
        print("No student information available.")
        return

    for key in ["Math Grade", "Science Grade", "English_Grade", "Final_Grade", "Category", "Status"]:
        if len(student_info[key]) != len(student_info["Name"]):
            print("Student record data is inconsistent.")
            return

    import pandas as pd
    df = pd.DataFrame(student_info)
    print("\nStudent Information : ")
    print(df)


def exit_program():
    again = input("Are you sure you want to exit? (Y/N): ").strip().upper()

    if again == "Y":
        print("Exiting the program....")
        global running
        running = False
    elif again == "N":
        print("Returning to the main menu....")
        return
    else:
        print("Invalid input. Please enter a valid option (Y/N).")
        exit_program()

running = True

while running:
    print("\n******************************************************")
    print("                  Student Management System           ")
    print("******************************************************")
    print("1. Add Student")
    print("2. Add Grades")
    print("3. View Student Info")
    print("4. Exit")
    print("******************************************************")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        input_student_info()

    elif choice == "2":
        add_grade()

    elif choice == "3":
        view_student_info()

    elif choice == "4":
        exit_program()

    else:
        print("Invalid Input! Please enter a valid option (1-4).")