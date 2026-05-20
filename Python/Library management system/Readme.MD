# 📚 Library Management System

A console-based Library Management System built with Python as part of a college assignment. It supports book management, student issuing/returning, admin login, fine calculation, and persistent data storage using JSON files.

---

## Features

- **Admin Login** – Secure login before accessing the system
- **Add Book** – Add new books or update quantity of existing ones
- **View Books** – Display all books in a formatted table
- **Search Book** – Search by Book ID, Book Name, or Author Name
- **Issue Book** – Issue a book to a student with date tracking
- **Return Book** – Return a book and auto-calculate overdue fine
- **Delete Book** – Remove a book from the library
- **Fine Calculation** – Rs. 5 per day after 15-day issue period
- **Persistent Storage** – Data saved in JSON files

---

## Project Structure

```
library-management/
│
├── main.py          # Main application file
├── books.json       # Stores book records (auto-created)
├── issued_books.json # Stores issued/returned records (auto-created)
├── README.md        # Project documentation
└── screenshots/     # Screenshots of the running app
```

---

## How to Run

Make sure you have **Python 3.x** installed.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/library-management.git

# Navigate to the folder
cd library-management

# Run the program
python main.py
```

---

## Admin Credentials

| Field    | Value    |
|----------|----------|
| Username | admin    |
| Password | lib@123  |

---

## Concepts Used

| Concept               | Where Used                            |
|-----------------------|---------------------------------------|
| Functions             | Each feature is a separate function   |
| Lists                 | Storing and iterating book records    |
| Dictionaries          | Each book/issue stored as a dict      |
| Loops                 | Menu loop, search iterations          |
| Conditional Statements| Validation, menu choices              |
| Exception Handling    | Input validation, file errors         |
| File Handling         | JSON read/write for persistence       |

---

## Sample Output

```
  Welcome to the Library Management System

========================================
        ADMIN LOGIN
========================================
  Username: admin
  Password: lib@123

  Login successful! Welcome, Admin.

========================================
     LIBRARY MANAGEMENT SYSTEM
========================================
  1. Add Book
  2. View All Books
  3. Search Book
  4. Issue Book
  5. Return Book
  6. Delete Book
  7. Exit
========================================
```

---

## Fine Calculation

- Books must be returned within **15 days**
- Fine: **Rs. 5 per day** after the due date
- Fine is shown at the time of return

---

## Author

**Your Name**  
Python Programming Assignment  
```