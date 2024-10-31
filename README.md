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
