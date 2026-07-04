import os
from student import Student

# File Path
FILE_PATH = "data/students.txt"

# Create data folder and file automatically
os.makedirs("data", exist_ok=True)

if not os.path.exists(FILE_PATH):
    open(FILE_PATH, "w").close()


# ------------------------------
# Add Student
# ------------------------------
def add_student(student):

    with open(FILE_PATH, "a") as file:
        file.write(student.to_record() + "\n")

    print("\nStudent Added Successfully.")


# ------------------------------
# Display Students
# ------------------------------
def display_students():

    with open(FILE_PATH, "r") as file:
        records = file.readlines()

    if not records:
        print("\nNo Student Records Found.")
        return

    print("\n" + "-" * 120)

    print(f"{'Roll No':<10}{'Name':<20}{'Email':<30}{'Phone':<15}{'Course':<25}{'CGPA':<8}")

    print("-" * 120)

    for record in records:

        data = record.strip().split(",")

        # Skip invalid records
        if len(data) != 6:
            print(f"Skipping invalid record: {record.strip()}")
            continue

        print(f"{data[0]:<10}{data[1]:<20}{data[2]:<30}{data[3]:<15}{data[4]:<25}{data[5]:<8}")

    print("-" * 120)
    
def search_student(rollno):

    with open(FILE_PATH, "r") as file:

        for record in file:

            data = record.strip().split(",")

            if len(data) != 6:
                continue 

            if data[0] == str(rollno):

                student = Student(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5]
                )

                return student

    return None
def delete_student(rollno):

    deleted = False

    with open(FILE_PATH, "r") as file:

        records = file.readlines()

    with open(FILE_PATH, "w") as file:

        for record in records:

            data = record.strip().split(",")

            if len(data) != 6:
                continue

            if data[0] != str(rollno):

                file.write(record)

            else:

                deleted = True

    return deleted
def update_student(updated_student):

    updated = False

    with open(FILE_PATH, "r") as file:

        records = file.readlines()

    with open(FILE_PATH, "w") as file:

        for record in records:

            data = record.strip().split(",")
            if len(data) != 6:
                continue

            if data[0] == str(updated_student.rollno):

                file.write(updated_student.to_record() + "\n")

                updated = True

            else:

                file.write(record)

    return updated
