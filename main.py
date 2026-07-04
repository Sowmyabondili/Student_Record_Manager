from student import Student
from utils import (
    validate_name,
    validate_email,
    validate_phone,
    validate_cgpa
)

from file_handler import (
    add_student,
    display_students,
    search_student,
    update_student,
    delete_student
)


# -----------------------------
# Add Student
# -----------------------------
def add_new_student():

    try:

        rollno = int(input("Enter Roll Number : "))

        if search_student(rollno):

            print("Student with this Roll Number already exists.")
            return

        name = input("Enter Name : ")

        if not validate_name(name):

            print("Invalid Name")
            return

        email = input("Enter Email : ")

        if not validate_email(email):

            print("Invalid Email")
            return

        phone = input("Enter Phone Number : ")

        if not validate_phone(phone):

            print("Invalid Phone Number")
            return

        course = input("Enter Interested Course : ")

        cgpa = input("Enter CGPA : ")

        if not validate_cgpa(cgpa):

            print("Invalid CGPA")
            return

        student = Student(
            rollno,
            name,
            email,
            phone,
            course,
            cgpa
        )

        add_student(student)

    except ValueError:

        print("Roll Number must be numeric.")


# -----------------------------
# Search Student
# -----------------------------
def search_record():

    rollno = input("Enter Roll Number : ")

    student = search_student(rollno)

    if student:

        print("\nStudent Found\n")

        student.display()

    else:

        print("Student Not Found")


# -----------------------------
# Update Student
# -----------------------------
def update_record():

    rollno = input("Enter Roll Number : ")

    student = search_student(rollno)

    if not student:

        print("Student Not Found.")
        return

    print("\nEnter New Details\n")

    name = input("Enter Name : ")

    if not validate_name(name):

        print("Invalid Name")
        return

    email = input("Enter Email : ")

    if not validate_email(email):

        print("Invalid Email")
        return

    phone = input("Enter Phone Number : ")

    if not validate_phone(phone):

        print("Invalid Phone Number")
        return

    course = input("Enter Interested Course : ")

    cgpa = input("Enter CGPA : ")

    if not validate_cgpa(cgpa):

        print("Invalid CGPA")
        return

    updated_student = Student(
        rollno,
        name,
        email,
        phone,
        course,
        cgpa
    )

    if update_student(updated_student):

        print("Student Updated Successfully.")

    else:

        print("Update Failed.")


# -----------------------------
# Delete Student
# -----------------------------
def delete_record():

    rollno = input("Enter Roll Number : ")

    if delete_student(rollno):

        print("Student Deleted Successfully.")

    else:

        print("Student Not Found.")


# -----------------------------
# Main Menu
# -----------------------------
while True:

    print("\n")
    print("=" * 50)
    print("      STUDENT RECORD MANAGER")
    print("=" * 50)

    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Exit")

    choice = input("\nEnter Choice : ")

    match choice:

        case "1":
            add_new_student()

        case "2":
            search_record()

        case "3":
            update_record()

        case "4":
            delete_record()

        case "5":
            display_students()

        case "6":
            print("\nThank You")
            break

        case _:
            print("Invalid Choice")