class Student:

    def __init__(self, rollno, name, email, phone, course, cgpa):
        self.rollno = rollno
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course
        self.cgpa = cgpa

    def to_record(self):
        """
        Convert the student object into a comma-separated string
        so it can be stored in students.txt
        """
        return f"{self.rollno},{self.name},{self.email},{self.phone},{self.course},{self.cgpa}"

    def display(self):
        """
        Display student details in a formatted way.
        """
        print(f"Roll Number : {self.rollno}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone}")
        print(f"Course      : {self.course}")
        print(f"CGPA        : {self.cgpa}")