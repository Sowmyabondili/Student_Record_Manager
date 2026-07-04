# 🎓 Student Record Manager

A **menu-driven Student Record Manager** developed in **Python** that demonstrates **Object-Oriented Programming (OOP)**, **File Handling**, **Regular Expressions (Regex)**, **Exception Handling**, and **CRUD (Create, Read, Update, Delete)** operations. The application allows users to efficiently manage student records through a simple command-line interface.

---

## 📌 Features

* ➕ Add Student Record
* 🔍 Search Student by Roll Number
* ✏️ Update Student Details
* ❌ Delete Student Record
* 📋 Display All Student Records
* 📧 Email Validation using Regular Expressions
* 📱 Phone Number Validation using Regular Expressions
* 👤 Name Validation using Regular Expressions
* 🎓 Store Interested Course
* 📊 CGPA Validation (0.0 – 10.0)
* 💾 File-based Data Storage
* ⚠️ Exception Handling for Invalid Inputs
* 🧩 Modular Python Program
* 🖥️ Menu-Driven Interface using `match-case`

---

## 🛠️ Technologies Used

* Python 3.10+
* Object-Oriented Programming (OOP)
* Regular Expressions (`re` module)
* File Handling
* Exception Handling
* Git & GitHub

---

## 📂 Project Structure

```text
Student_Record_Manager/
│
├── data/
│   └── students.txt
│
├── .gitignore
├── file_handler.py
├── main.py
├── student.py
├── utils.py
└── README.md
```

---

## 📖 Student Information Stored

Each student record contains:

* Roll Number
* Name
* Email
* Phone Number
* Interested Course
* CGPA

### Example Record

```text
101,Sowmya,sowmya@gmail.com,9876543210,Data Science,8.75
```

---

## 📋 Menu

```text
==================================================
        STUDENT RECORD MANAGER
==================================================

1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display Students
6. Exit
```

---

## 🧠 Concepts Implemented

### Object-Oriented Programming

* Class
* Object
* Constructor (`__init__`)
* Encapsulation

### File Handling

* Create File
* Read File
* Write File
* Update Records
* Delete Records

### Regular Expressions (Regex)

* Email Validation
* Phone Number Validation
* Name Validation

### Exception Handling

* `ValueError`
* Input Validation

### CRUD Operations

* Create Student
* Read Student
* Update Student
* Delete Student

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Sowmyabondili/Student_Record_Manager.git
```

2. Navigate to the project folder:

```bash
cd Student_Record_Manager
```

3. Run the application:

```bash
python main.py
```

---

## 📸 Sample Output

```text
==================================================
        STUDENT RECORD MANAGER
==================================================

1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display Students
6. Exit

Enter Choice:
```

---

## 🎯 Learning Outcomes

This project helped me understand:

* Object-Oriented Programming in Python
* File Handling Techniques
* Regular Expressions for Input Validation
* Exception Handling
* CRUD Operations
* Modular Programming
* Menu-Driven Application Development
* Version Control using Git and GitHub

---

## 🚀 Future Enhancements

* Store records using SQLite/MySQL database
* Export records to CSV/Excel
* Graphical User Interface (Tkinter)
* Web-based version using Flask or Django
* User Authentication System
* Advanced Search and Filtering

---

## 👨‍💻 Author

**Sowmya Bondili**

B.Tech – Artificial Intelligence & Data Science

Python Developer | Machine Learning Enthusiast

GitHub: https://github.com/Sowmyabondili
