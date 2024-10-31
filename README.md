# Student Result Management System

The **Student Result Management System** is a comprehensive solution built in Python, designed to store and manage student information and results in an organized, accessible way. Originally built as a Tkinter-based desktop GUI application, it was later adapted into a Flask web app to provide remote accessibility and ease of use. The application includes user authentication, a secure login system, and password recovery options, as well as options to add, view, and manage student records and results.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **User Authentication**: Secure login system, with a “Forgot Password” feature for user convenience.
- **SQLite Database Integration**: Data is stored persistently using SQLite, making it simple and lightweight.
- **Student Management**: Add, edit, and view student records through an intuitive interface.
- **Results Tracking**: Easily manage and display results for each student in the system.
- **Aesthetic UI**: Designed for a clean and user-friendly experience, with customization for an appealing look.
- **Web-Based with Flask**: Allows users to access the application from any web browser, making it versatile and accessible.

---

## Project Structure

The project follows a standard structure for Flask applications, with separate folders for templates (HTML files) and static assets (CSS and JavaScript).

```plaintext
Student-Result-Management-System/
├── app.py                    # Main Flask application file
├── templates/                # HTML templates for Flask
│   ├── home.html             # Home page after login
│   ├── login.html            # Login page with Forgot Password option
│   ├── register.html         # Register new user page
│   └── add_result.html       # Form page for adding student results
├── static/                   # Static files for CSS, JavaScript, images, etc.
│   ├── styles.css            # Main stylesheet
│   └── scripts.js            # Main JavaScript file
├── requirements.txt          # Project dependencies
└── students.db               # SQLite database file

# Student Result Management System

The **Student Result Management System** is a Python-based project designed to manage student records and results efficiently. It features user authentication, result management, and database integration with SQLite, offering a user-friendly interface for students and administrators.

---

## Features

- **User Authentication**: Secure login with a "Forgot Password" feature.
- **SQLite Database Integration**: Data is stored in an SQLite database, making the application portable and lightweight.
- **Student and Result Management**: Easily add, view, edit, and delete student records and results.
- **Aesthetic UI**: Built with Tkinter for a desktop GUI, styled to be clean and visually appealing.

---

## Table of Contents

- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Setup and Installation

### Prerequisites

- **Python 3.x** installed on your machine.
- Basic knowledge of Python and Flask for customization if needed.

### Step-by-Step Installation Guide

1. **Clone the Repository**  
   Clone this repository to your local machine.
   ```bash
   git clone https://github.com/Abhi0pal/Student-Result-Management-System.git
   cd Student-Result-Management-System


🚀 Usage
User Authentication and Registration

    Login: Log in with your username and password.
    Forgot Password: Use the "Forgot Password" option to reset your password.
    Register: Create a new user account if you’re a first-time user.

Managing Student Results

    Add Results: Enter a student’s name and score to add a new record.
    View Results: View all student records in a tabulated format.
    Edit/Delete Results: Modify or delete entries as needed.




