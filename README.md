<h1 align="center" id="title"># Student Result Management System - Software Requirements Specification (SRS)</h1>

<p align="center"><img src="https://socialify.git.ci/Abhi0pal/Student-Result-Management/image?description=1&amp;descriptionEditable=The%20purpose%20of%20this%20document%20is%20to%20outline%20the%20functional%20and%20non-functional%20requirements%20for%20the%20Student%20Result%20Management%20System.%20The%20system%20will%20facilitate%20the%20efficient%20management%20of%20student%20academic%20records%2C%20featuring%20user%20authentication%2C%20CRUD%20operations%20for%20student%20results%2C%20and%20secure%20data%20storage.%20It%20will%20provide%20an%20intuitive%20and%20visually%20appealing%20interface%20built%20using%20Python%27s%20Tkinter%20and%20use%20SQLite%20for%20secure%20data%20management&amp;font=Inter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Solid&amp;pulls=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">The purpose of this document is to outline the functional and non-functional requirements for the Student Result Management System. The system will facilitate the efficient management of student academic records featuring user authentication CRUD operations for student results and secure data storage. It will provide an intuitive and visually appealing interface built using Python's Tkinter and use SQLite for secure data management.</p>

<h2>Project Screenshots:</h2>
<p>

<img src="https://storeassets.im-cdn.com/products/e2023e/19Xzr64TTOSDkIiYNDNr_Screenshot%20(1284)_0x0_webp.png" alt="project-screenshot" width="400" height="400/">



<img src="https://storeassets.im-cdn.com/products/e2023e/qJ67e60HRDqf7WYpQIHG_Screenshot%20(1282)_0x0_webp.png" alt="project-screenshot" width="400" height="400/">

<img src="https://storeassets.im-cdn.com/products/e2023e/KDoO2eatQyuZxmx7nvAC_Screenshot%20(1280)_0x0_webp.png" alt="project-screenshot" width="400" height="400/">



<img src="https://storeassets.im-cdn.com/products/e2023e/tuoiAno4RRmFcdi7gELt_Screenshot%20(1279)_0x0_webp.png" alt="project-screenshot" width="400" height="400/">

  </p>
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   User Authentication: Secure login registration and password recovery.
*   Result Management: CRUD operations for student records
*   Data Security: Hashed passwords and input validation to ensure safety.
*   Aesthetic Design: A user-friendly and visually appealing interface.




## 1. Introduction

### 1.1 Purpose
The purpose of this document is to define the functional and non-functional requirements for the Student Result Management System. The system will enable efficient management of student academic records, providing features like user authentication, adding, viewing, editing, and deleting student results. The software will offer an intuitive and aesthetically pleasing user interface using Tkinter and store data securely using SQLite.

### 1.2 Scope
The Student Result Management System is designed for educational institutions to automate and simplify the process of managing student records. It will include functionalities for user authentication, result management, and secure data storage. The system will also feature an attractive and user-friendly design. Future enhancements will consider role-based access, reporting, automated grading, and improved security measures.

### 1.3 Definitions, Acronyms, and Abbreviations
- **GUI**: Graphical User Interface
- **SQLite**: A lightweight relational database management system
- **CRUD**: Create, Read, Update, and Delete
- **Tkinter**: Python’s standard GUI toolkit
- **Hashed Passwords**: Passwords stored in an encrypted format for security

### 1.4 References
- [Python 3.x Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## 2. Overall Description

### 2.1 Product Perspective
The Student Result Management System is a standalone software application. It serves as a replacement for manual record-keeping and is intended to be a desktop-based application with a simple and easy-to-use interface. The system will be built using Python and leverage Tkinter for the GUI and SQLite for database management.

### 2.2 Product Features
- **User Authentication**: Secure login, registration, and password recovery.
- **Result Management**: Add, view, update, or delete student records.
- **Data Security**: Passwords will be hashed to ensure data protection.
- **Aesthetic Design**: The user interface will be visually appealing and easy to navigate.

### 2.3 User Classes and Characteristics
- **Admin User**: Has full access to all functionalities, including managing student records and user accounts.
- **General User**: Can only view results and may have limited access, depending on future role-based implementation.

### 2.4 Operating Environment
- **Platform**: Windows, macOS, Linux
- **Programming Language**: Python 3.x
- **Database**: SQLite
- **Dependencies**: Tkinter, SQLite3

### 2.5 Design and Implementation Constraints
- The system must be implemented in Python using the Tkinter library.
- Data must be stored in an SQLite database.
- Passwords must be securely hashed and not stored in plain text.

### 2.6 Assumptions and Dependencies
- Users must have Python 3.x installed on their system.
- Users should have basic knowledge of how to run Python scripts.
- Dependencies listed in `requirements.txt` must be installed for the system to work correctly.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Authentication
- **Login**: Users must be able to log in using their username and password.
- **Register**: New users must be able to create an account with a unique username and secure password.
- **Forgot Password**: Users must be able to reset their password if forgotten.

#### 3.1.2 Manage Student Results
- **Add Result**: Admin users can add new student records by entering the student’s name and score.
- **View Results**: All users can view student records in a table.
- **Edit Result**: Admin users can update existing student records.
- **Delete Result**: Admin users can remove student records as necessary.

#### 3.1.3 Database Management
- The system must use an SQLite database named `students.db`.
- **Tables**:
  - **Users Table**
    - `id`: Primary Key, Integer
    - `username`: Text, unique
    - `password`: Text, hashed
  - **Results Table**
    - `id`: Primary Key, Integer
    - `name`: Text
    - `score`: Integer

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance
- The system should be responsive and handle user actions quickly.
- Database queries should execute efficiently to ensure a smooth user experience.

#### 3.2.2 Usability
- The user interface must be intuitive and easy to use for non-technical users.
- The system must have clear labels and instructions for each functionality.

#### 3.2.3 Security
- Passwords must be hashed to protect user credentials.
- The system must validate all user inputs to prevent SQL injection attacks.

#### 3.2.4 Maintainability
- The code should be modular and well-documented for easy maintenance and future enhancements.
- Use a version control system (e.g., Git) to track changes and collaborate effectively.

## 4. External Interface Requirements

### 4.1 User Interfaces
- **Login Page**: Form for user authentication with options for registration and password recovery.
- **Main Dashboard**: Overview of available functionalities with options to manage student results.
- **Result Table**: Displays all student records with options to edit or delete entries.

### 4.2 Hardware Interfaces
- A standard computer with a keyboard and mouse is sufficient for using the system.

### 4.3 Software Interfaces
- **Python**: The main programming language for the system.
- **SQLite**: The database management system for storing records.

### 4.4 Communication Interfaces
- The system will run locally and will not require network communication.

## 5. Other Requirements

### 5.1 Future Enhancements
- Implement role-based access for different user levels (admin vs. general user).
- Add reporting features for exporting student data.
- Automate grading based on pre-defined criteria.
- Improve the UI with advanced styling libraries for a modern look.
- Enhance security measures, including better session management and data encryption.

## 6. Appendices

### 6.1 Sample Code for Database Initialization
```python
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
conn.commit()
conn.close()
