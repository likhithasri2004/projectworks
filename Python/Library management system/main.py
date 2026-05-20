# main.py

import json
import os
from datetime import date
from datetime import datetime

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "lib@123"
USERS_FILE = "users.json"
BOOKS_FILE = "books.json"
ISSUED_FILE = "issued_books.json"
FINE_PER_DAY = 5

# ── File Helpers ──

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_users(users):
    try:
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
    except IOError as e:
        print(f"  [!] Error saving users: {e}")

# ── Menu ──

def show_menu():
    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Admin Login")
    print("  2. Register")
    print("  3. User Login")
    print("  4. Exit")
    print("=" * 40)

# ── Admin Login ──

def admin_login():
    print("\n" + "=" * 40)
    print("          ADMIN LOGIN")
    print("=" * 40)
    attempts = 3
    while attempts > 0:
        username = input("  Username: ").strip()
        password = input("  Password: ").strip()
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\n  Login successful! Welcome, Admin.\n")
            return True
        else:
            attempts -= 1
            print(f"  [!] Wrong credentials. {attempts} attempt(s) left.")
    print("\n  Too many failed attempts. Going back...\n")
    return False

# ── Register ──

def user_register():
    print("\n" + "=" * 40)
    print("          USER REGISTER")
    print("=" * 40)
    users = load_users()

    full_name = input("  Enter your full name: ").strip()
    if not full_name:
        print("  [!] Name cannot be empty.")
        return

    student_id = input("  Enter your student ID: ").strip()
    if not student_id:
        print("  [!] Student ID cannot be empty.")
        return

    for user in users:
        if user["student_id"] == student_id:
            print("  [!] Student ID already registered.")
            return

    username = input("  Choose a username: ").strip()
    if not username:
        print("  [!] Username cannot be empty.")
        return

    for user in users:
        if user["username"].lower() == username.lower():
            print("  [!] Username already taken.")
            return

    password = input("  Choose a password: ").strip()
    if len(password) < 4:
        print("  [!] Password must be at least 4 characters.")
        return

    confirm = input("  Confirm password: ").strip()
    if password != confirm:
        print("  [!] Passwords do not match.")
        return

    new_user = {
        "full_name": full_name,
        "student_id": student_id,
        "username": username,
        "password": password,
        "registered_on": date.today().strftime("%Y-%m-%d")
    }
    users.append(new_user)
    save_users(users)

    print(f"\n  Registered successfully!")
    print(f"  Name      : {full_name}")
    print(f"  Student ID: {student_id}")
    print(f"  Username  : {username}")
    print(f"  You can now login.")

# ── User Login ──

def user_login():
    print("\n" + "=" * 40)
    print("           USER LOGIN")
    print("=" * 40)
    users = load_users()

    if not users:
        print("  [!] No users registered yet. Please register first.")
        return None

    attempts = 3
    while attempts > 0:
        username = input("  Username: ").strip()
        password = input("  Password: ").strip()
        for user in users:
            if user["username"].lower() == username.lower() and user["password"] == password:
                print(f"\n  Welcome, {user['full_name']}!\n")
                return user
        attempts -= 1
        print(f"  [!] Wrong credentials. {attempts} attempt(s) left.")

    print("\n  Too many failed attempts. Going back...\n")
    return None

# ── Book File Helpers ──

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_books(books):
    try:
        with open(BOOKS_FILE, "w") as f:
            json.dump(books, f, indent=4)
    except IOError as e:
        print(f"  [!] Error saving books: {e}")

def generate_book_id(books):
    if not books:
        return "B001"
    last_id = max(int(b["book_id"][1:]) for b in books)
    return f"B{str(last_id + 1).zfill(3)}"

def print_separator():
    print("-" * 55)

def print_book_header():
    print_separator()
    print(f"  {'ID':<6} {'Book Name':<22} {'Author':<15} {'Qty'}")
    print_separator()

def print_book_row(book):
    print(f"  {book['book_id']:<6} {book['book_name'][:21]:<22} {book['author_name'][:14]:<15} {book['quantity']}")

# ── Add Book ──

def add_book():
    print("\n--- Add New Book ---")
    books = load_books()

    book_name = input("  Enter book name: ").strip()
    if not book_name:
        print("  [!] Book name cannot be empty.")
        return

    author_name = input("  Enter author name: ").strip()
    if not author_name:
        print("  [!] Author name cannot be empty.")
        return

    while True:
        try:
            quantity = int(input("  Enter quantity: ").strip())
            if quantity <= 0:
                print("  [!] Quantity must be a positive number.")
                continue
            break
        except ValueError:
            print("  [!] Please enter a valid number.")

    for book in books:
        if book["book_name"].lower() == book_name.lower() and \
           book["author_name"].lower() == author_name.lower():
            book["quantity"] += quantity
            save_books(books)
            print(f"\n  Book exists. Quantity updated to {book['quantity']}.")
            return

    book_id = generate_book_id(books)
    new_book = {
        "book_id": book_id,
        "book_name": book_name,
        "author_name": author_name,
        "quantity": quantity
    }
    books.append(new_book)
    save_books(books)
    print(f"\n  Book added! ID: {book_id}")

# ── View Books ──

def view_books():
    print("\n--- All Books ---")
    books = load_books()
    if not books:
        print("  No books in the library.")
        return
    print_book_header()
    for book in books:
        print_book_row(book)
    print_separator()
    print(f"  Total: {len(books)} book(s)")

# ── Search Book ──

def search_book():
    print("\n--- Search Book ---")
    print("  1. Search by Book ID")
    print("  2. Search by Book Name")
    print("  3. Search by Author Name")

    choice = input("\n  Enter choice: ").strip()
    books = load_books()
    results = []

    if choice == "1":
        book_id = input("  Enter Book ID: ").strip()
        results = [b for b in books if book_id.lower() in b["book_id"].lower()]
    elif choice == "2":
        name = input("  Enter Book Name: ").strip().lower()
        results = [b for b in books if name in b["book_name"].lower()]
    elif choice == "3":
        author = input("  Enter Author Name: ").strip().lower()
        results = [b for b in books if author in b["author_name"].lower()]
    else:
        print("  [!] Invalid choice.")
        return

    if not results:
        print("  No matching books found.")
        return

    print(f"\n  {len(results)} result(s) found:")
    print_book_header()
    for book in results:
        print_book_row(book)
    print_separator()

# ── Issue & Return Helpers ──

def load_issued():
    if not os.path.exists(ISSUED_FILE):
        return []
    try:
        with open(ISSUED_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_issued(issued):
    try:
        with open(ISSUED_FILE, "w") as f:
            json.dump(issued, f, indent=4)
    except IOError as e:
        print(f"  [!] Error saving issued records: {e}")

def find_book_by_id(books, book_id):
    for book in books:
        if book["book_id"].lower() == book_id.lower():
            return book
    return None

# ── Issue Book ──

def issue_book(logged_in_user=None):
    print("\n--- Issue Book ---")
    books = load_books()
    issued = load_issued()

    book_id = input("  Enter Book ID to issue: ").strip()
    book = find_book_by_id(books, book_id)

    if not book:
        print("  [!] Book not found.")
        return

    if book["quantity"] <= 0:
        print("  [!] Book is out of stock.")
        return

    if logged_in_user:
        student_name = logged_in_user["full_name"]
        student_id = logged_in_user["student_id"]
        print(f"  Issuing to: {student_name} ({student_id})")
    else:
        student_name = input("  Enter student name: ").strip()
        if not student_name:
            print("  [!] Name cannot be empty.")
            return
        student_id = input("  Enter student ID: ").strip()
        if not student_id:
            print("  [!] Student ID cannot be empty.")
            return

    for record in issued:
        if record["student_id"] == student_id and \
           record["book_id"].lower() == book_id.lower() and \
           record["status"] == "issued":
            print("  [!] This book is already issued to this student.")
            return

    issue_date = date.today().strftime("%Y-%m-%d")
    record = {
        "issue_id": f"ISS{len(issued) + 1:03d}",
        "book_id": book["book_id"],
        "book_name": book["book_name"],
        "student_name": student_name,
        "student_id": student_id,
        "issue_date": issue_date,
        "return_date": None,
        "status": "issued"
    }

    issued.append(record)
    book["quantity"] -= 1
    save_books(books)
    save_issued(issued)

    print(f"\n  Issued successfully!")
    print(f"  Issue ID : {record['issue_id']}")
    print(f"  Book     : {book['book_name']}")
    print(f"  Student  : {student_name} ({student_id})")
    print(f"  Date     : {issue_date}")
    print(f"  Note     : Return within 15 days to avoid fine.")

# ── Return Book ──

def return_book():
    print("\n--- Return Book ---")
    issued = load_issued()
    books = load_books()

    issue_id = input("  Enter Issue ID: ").strip()
    record = None

    for r in issued:
        if r["issue_id"].lower() == issue_id.lower():
            record = r
            break

    if not record:
        print("  [!] Issue record not found.")
        return

    if record["status"] == "returned":
        print("  [!] This book is already returned.")
        return

    return_date = date.today()
    issue_date = datetime.strptime(record["issue_date"], "%Y-%m-%d").date()
    days_held = (return_date - issue_date).days

    fine = 0
    if days_held > 15:
        overdue_days = days_held - 15
        fine = overdue_days * FINE_PER_DAY
        print(f"\n  Overdue by {overdue_days} day(s). Fine: Rs. {fine}")
    else:
        print("\n  Returned on time. No fine.")

    record["return_date"] = return_date.strftime("%Y-%m-%d")
    record["status"] = "returned"
    record["fine"] = fine
    record["days_held"] = days_held

    book = find_book_by_id(books, record["book_id"])
    if book:
        book["quantity"] += 1

    save_issued(issued)
    save_books(books)

    print(f"\n  Returned successfully!")
    print(f"  Book     : {record['book_name']}")
    print(f"  Student  : {record['student_name']}")
    print(f"  Days held: {days_held}")
    if fine > 0:
        print(f"  Fine paid: Rs. {fine}")

# ── Delete Book ──

def delete_book():
    print("\n--- Delete Book ---")
    books = load_books()

    book_id = input("  Enter Book ID to delete: ").strip()
    book = find_book_by_id(books, book_id)

    if not book:
        print("  [!] Book not found.")
        return

    print(f"\n  Found: {book['book_name']} by {book['author_name']}")
    confirm = input("  Confirm delete? (yes/no): ").strip().lower()

    if confirm == "yes":
        books = [b for b in books if b["book_id"].lower() != book_id.lower()]
        save_books(books)
        print("  Book deleted successfully.")
    else:
        print("  Delete cancelled.")

# ── My Issued Books ──

def my_issued_books(logged_in_user):
    print("\n--- My Issued Books ---")
    issued = load_issued()
    my_records = [r for r in issued if r["student_id"] == logged_in_user["student_id"]]

    if not my_records:
        print("  You have no issued books.")
        return

    print_separator()
    print(f"  {'Issue ID':<10} {'Book Name':<22} {'Date':<12} {'Status'}")
    print_separator()
    for r in my_records:
        print(f"  {r['issue_id']:<10} {r['book_name'][:21]:<22} {r['issue_date']:<12} {r['status']}")
    print_separator()

# ── Admin Menu ──

def admin_menu():
    while True:
        print("\n" + "=" * 40)
        print("          ADMIN PANEL")
        print("=" * 40)
        print("  1. Add Book")
        print("  2. View All Books")
        print("  3. Search Book")
        print("  4. Issue Book")
        print("  5. Return Book")
        print("  6. Delete Book")
        print("  7. Logout")
        print("=" * 40)

        choice = input("  Enter your choice (1-7): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("\n  Admin logged out.")
            break
        else:
            print("  [!] Invalid choice.")

        input("\n  Press Enter to continue...")

# ── User Menu ──

def user_menu(logged_in_user):
    while True:
        print("\n" + "=" * 40)
        print(f"  Hello, {logged_in_user['full_name']}")
        print("=" * 40)
        print("  1. View All Books")
        print("  2. Search Book")
        print("  3. Issue Book")
        print("  4. Return Book")
        print("  5. My Issued Books")
        print("  6. Logout")
        print("=" * 40)

        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            view_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book(logged_in_user)
        elif choice == "4":
            return_book()
        elif choice == "5":
            my_issued_books(logged_in_user)
        elif choice == "6":
            print(f"\n  Goodbye, {logged_in_user['full_name']}!")
            break
        else:
            print("  [!] Invalid choice.")

        input("\n  Press Enter to continue...")

# ── Main ──

def main():
    print("\n  Welcome to Library Management System")
    while True:
        show_menu()
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            if admin_login():
                admin_menu()
        elif choice == "2":
            user_register()
            input("\n  Press Enter to continue...")
        elif choice == "3":
            user = user_login()
            if user:
                user_menu(user)
        elif choice == "4":
            print("\n  Thank you! Goodbye.\n")
            break
        else:
            print("  [!] Invalid choice.")

if __name__ == "__main__":
    main()