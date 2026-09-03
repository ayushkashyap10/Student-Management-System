# 🎓 Student Management System

A simple **Command-Line Student Management System** built with Python.

This project allows users to manage student records through a clean and interactive CLI. Student data is stored persistently in a text file, so existing records are automatically loaded when the program starts.

---

## ✨ Features

* ➕ Add new student records
* 📋 View all student records
* 🔍 Search students by registration number
* ✏️ Update student information
* 🗑️ Delete student records
* 💾 Persistent data storage using `students.txt`
* ✅ Registration number uniqueness checking
* 🛡️ Input validation and error handling
* 🖥️ Interactive Command-Line Interface

---

## 📌 Student Information

Each student record contains:

| Field               | Description                |
| ------------------- | -------------------------- |
| Registration Number | Unique student identifier  |
| Name                | Student's name             |
| Age                 | Student's age              |
| Program             | Student's academic program |
| CGPA                | Student's current CGPA     |

---

## 🛠️ Technologies Used

* **Python**
* **Lists**
* **Dictionaries**
* **File Handling**
* **Exception Handling**
* **Command-Line Interface (CLI)**

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── students.txt
└── README.md
```

---

## ⚙️ How It Works

The application stores student records in a Python list containing dictionaries.

Example:

```python
{
    "regno": 12505643,
    "name": "Ayush",
    "age": 18,
    "program": "computer science and engineering",
    "cgpa": 8.39
}
```

The records are saved in `students.txt` using the following format:

```text
Registration Number | Name | Age | Program | CGPA
```

When the application starts, existing records are loaded automatically from the file.

Updates and deletions rewrite the file to keep the stored records synchronized with the current data.

---

## 🎯 Available Operations

```text
============== MENU ===============

1) Add Student
2) View All Students
3) Search Student
4) Update Student Record
5) Delete Student Record
6) Exit

===================================
```

### 1. Add Student

Allows the user to enter:

* Registration number
* Name
* Age
* Program
* CGPA

The system checks whether the registration number already exists before adding the student.

### 2. View Students

Displays all students currently stored in the system.

### 3. Search Student

Searches for a student using their registration number.

### 4. Update Student

Allows modification of:

* Name
* Age
* Program
* CGPA

### 5. Delete Student

Deletes a student record after confirmation.

### 6. Exit

Closes the application.

---

## 🚀 How to Run

### Prerequisites

Make sure **Python 3** is installed on your system.

Check your Python installation:

```bash
python --version
```

### Run the Project

Clone the repository:

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

Navigate to the project folder:

```bash
cd Student-Management-System
```

Run the program:

```bash
python main.py
```

---

## 💾 Data Storage

This project uses a simple text file for persistent storage.

```text
students.txt
```

The application automatically:

1. Loads existing records when started.
2. Stores newly added students.
3. Updates the file after modifying records.
4. Rewrites the file after deleting records.

---

## 🧠 Concepts Demonstrated

This project demonstrates practical use of fundamental Python concepts:

* Variables and data types
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* File handling
* Exception handling
* Input validation
* CRUD operations
* Basic data persistence

---

## 📸 Project Preview

Add a screenshot of your running CLI here:

```markdown
![Student Management System](screenshot.png)
```

---

## 🔮 Future Improvements

Possible future versions could include:

* SQLite database integration
* Graphical User Interface (GUI)
* Student sorting and filtering
* Attendance management
* Marks and grade management
* Export records to CSV
* Login/authentication system
* Student statistics and analytics

---

## 👨‍💻 Author

**Ayush**

B.Tech Computer Science & Engineering Student

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
