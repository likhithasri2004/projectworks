#  Basic menu system with loops

def display_menu():
    print("\n" + "="*50)
    print("        🏦 BANK MANAGEMENT SYSTEM 🏦")
    print("="*50)
    print("1. Create Account")
    print("2. Exit")
    print("="*50)

def main():
    print("\n🌟 Welcome to the Bank Management System 🌟")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            print("\n✅ Create Account feature - Coming soon!")
        elif choice == '2':
            print("\n👋 Thank you for using the system!")
            break
        else:
            print("❌ Invalid choice!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

    # Account creation

accounts = []  

def display_menu():
    print("\n" + "="*50)
    print("        🏦 BANK MANAGEMENT SYSTEM 🏦")
    print("="*50)
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Exit")
    print("="*50)

def create_account():
    print("\n--- Create New Account ---")
    
    name = input("Enter Account Holder Name: ").strip().title()
    mobile = input("Enter Mobile Number (10 digits): ").strip()
    initial_deposit = float(input("Enter Initial Deposit (Min ₹500): "))
    
    # Simple validation
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile number!")
        return
    
    if initial_deposit < 500:
        print("❌ Minimum deposit is ₹500!")
        return
    
    # Generate account number
    acc_number = len(accounts) + 1001
    
    account = {
        'number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': initial_deposit
    }
    
    accounts.append(account)
    print(f"\n✅ Account Created! Account Number: {acc_number}")

def view_accounts():
    if not accounts:
        print("\n❌ No accounts found!")
        return
    
    print("\n--- All Accounts ---")
    for acc in accounts:
        print(f"Acc: {acc['number']} | {acc['name']} | ₹{acc['balance']}")

def main():
    print("\n🌟 Welcome!")
    
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            view_accounts()
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid!")
        
        input("\nPress Enter...")

if __name__ == "__main__":
    main()

    # Switch to dictionary + Search Account

    # Using dictionaries for faster lookup

accounts = {}  # account_number -> account details

def generate_acc_number():
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def create_account():
    print("\n--- Create Account ---")
    
    name = input("Name: ").strip().title()
    mobile = input("Mobile (10 digits): ").strip()
    
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile!")
        return
    
    try:
        deposit = float(input("Initial deposit (Min ₹500): "))
        if deposit < 500:
            print("❌ Minimum ₹500 required!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    acc_number = generate_acc_number()
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': deposit,
        'pin': '1234'  # Default PIN
    }
    
    print(f"\n✅ Account {acc_number} created! PIN: 1234")

def find_account():
    acc_num = input("Enter account number: ").strip()
    if acc_num in accounts:
        return accounts[acc_num]
    else:
        print("❌ Account not found!")
        return None

def view_account():
    account = find_account()
    if account:
        print(f"\nAccount: {account['account_number']}")
        print(f"Name: {account['name']}")
        print(f"Mobile: {account['mobile']}")
        print(f"Balance: ₹{account['balance']}")

def display_menu():
    print("\n" + "="*40)
    print("1. Create Account")
    print("2. View Account")
    print("3. Exit")

def main():
    global accounts
    
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            view_account()
        elif choice == '3':
            break
        else:
            print("Invalid!")
        
        input("\nPress Enter...")

if __name__ == "__main__":
    main()

    #  PIN authentication added
from getpass import getpass

accounts = {}

def generate_acc_number():
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def authenticate():
    print("\n--- Login ---")
    acc_num = input("Account number: ").strip()
    
    if acc_num not in accounts:
        print("❌ Account not found!")
        return None
    
    pin = getpass("Enter PIN: ").strip()
    
    if accounts[acc_num]['pin'] == pin:
        print(f"✅ Welcome {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("❌ Wrong PIN!")
        return None

def create_account():
    print("\n--- Create Account ---")
    name = input("Name: ").strip().title()
    mobile = input("Mobile: ").strip()
    
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile!")
        return
    
    try:
        deposit = float(input("Initial deposit (₹500 min): "))
        if deposit < 500:
            print("❌ Minimum ₹500!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    acc_number = generate_acc_number()
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': deposit,
        'pin': '1234'
    }
    
    print(f"\n✅ Account {acc_number} created! Default PIN: 1234")

def check_balance():
    account = authenticate()
    if account:
        print(f"\n💰 Balance: ₹{account['balance']:.2f}")

def display_menu():
    print("\n" + "="*40)
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()

    # Deposit and Withdraw functions   
from getpass import getpass

accounts = {}

def generate_acc_number():
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def authenticate():
    acc_num = input("Account number: ").strip()
    if acc_num not in accounts:
        print("❌ Account not found!")
        return None
    
    pin = getpass("PIN: ").strip()
    if accounts[acc_num]['pin'] == pin:
        print(f"✅ Welcome {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("❌ Wrong PIN!")
        return None

def create_account():
    print("\n--- Create Account ---")
    name = input("Name: ").strip().title()
    mobile = input("Mobile: ").strip()
    
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile!")
        return
    
    try:
        deposit = float(input("Initial deposit (₹500 min): "))
        if deposit < 500:
            print("❌ Minimum ₹500!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    acc_number = generate_acc_number()
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': deposit,
        'pin': '1234'
    }
    
    print(f"\n✅ Account {acc_number} created!")

def deposit():
    account = authenticate()
    if not account:
        return
    
    try:
        amount = float(input("Deposit amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        account['balance'] += amount
        print(f"✅ Deposited ₹{amount:.2f}")
        print(f"💰 New balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def withdraw():
    account = authenticate()
    if not account:
        return
    
    try:
        amount = float(input("Withdraw amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        if amount > account['balance']:
            print(f"❌ Insufficient! Available: ₹{account['balance']:.2f}")
            return
        
        account['balance'] -= amount
        print(f"✅ Withdrew ₹{amount:.2f}")
        print(f"💰 Remaining: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def check_balance():
    account = authenticate()
    if account:
        print(f"\n💰 Balance: ₹{account['balance']:.2f}")

def display_menu():
    print("\n" + "="*40)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()

  # Add File Storage

  #  Data saved to file!
import json
import os
from getpass import getpass

ACCOUNTS_FILE = "accounts.txt"

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    
    with open(ACCOUNTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return {}

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def generate_acc_number(accounts):
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def authenticate(accounts):
    acc_num = input("Account number: ").strip()
    if acc_num not in accounts:
        print("❌ Account not found!")
        return None
    
    pin = getpass("PIN: ").strip()
    if accounts[acc_num]['pin'] == pin:
        print(f"✅ Welcome {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("❌ Wrong PIN!")
        return None

def create_account(accounts):
    print("\n--- Create Account ---")
    name = input("Name: ").strip().title()
    mobile = input("Mobile: ").strip()
    
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile!")
        return
    
    try:
        deposit = float(input("Initial deposit (₹500 min): "))
        if deposit < 500:
            print("❌ Minimum ₹500!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    acc_number = generate_acc_number(accounts)
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': deposit,
        'pin': '1234'
    }
    
    save_accounts(accounts)
    print(f"\n✅ Account {acc_number} created! PIN: 1234")

def deposit(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    try:
        amount = float(input("Deposit amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        account['balance'] += amount
        save_accounts(accounts)
        print(f"✅ Deposited ₹{amount:.2f}")
        print(f"💰 New balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def withdraw(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    try:
        amount = float(input("Withdraw amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        if amount > account['balance']:
            print(f"❌ Insufficient! Available: ₹{account['balance']:.2f}")
            return
        
        account['balance'] -= amount
        save_accounts(accounts)
        print(f"✅ Withdrew ₹{amount:.2f}")
        print(f"💰 Remaining: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def check_balance(accounts):
    account = authenticate(accounts)
    if account:
        print(f"\n💰 Balance: ₹{account['balance']:.2f}")

def display_menu():
    print("\n" + "="*40)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

def main():
    accounts = load_accounts()
    
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main() 

#  Add Transaction Logging
# main_v7.py - Transaction history added
import json
import os
from getpass import getpass
from datetime import datetime

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return {}

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def log_transaction(acc_number, trans_type, amount, balance):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{timestamp} | Acc: {acc_number} | {trans_type}: ₹{amount} | Balance: ₹{balance}\n"
    
    with open(TRANSACTIONS_FILE, 'a') as f:
        f.write(log)

def generate_acc_number(accounts):
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def authenticate(accounts):
    acc_num = input("Account number: ").strip()
    if acc_num not in accounts:
        print("❌ Account not found!")
        return None
    
    pin = getpass("PIN: ").strip()
    if accounts[acc_num]['pin'] == pin:
        print(f"✅ Welcome {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("❌ Wrong PIN!")
        return None

def create_account(accounts):
    print("\n--- Create Account ---")
    name = input("Name: ").strip().title()
    mobile = input("Mobile: ").strip()
    
    if len(mobile) != 10 or not mobile.isdigit():
        print("❌ Invalid mobile!")
        return
    
    try:
        deposit = float(input("Initial deposit (₹500 min): "))
        if deposit < 500:
            print("❌ Minimum ₹500!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    acc_number = generate_acc_number(accounts)
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'balance': deposit,
        'pin': '1234'
    }
    
    save_accounts(accounts)
    log_transaction(acc_number, "Account Created", deposit, deposit)
    print(f"\n✅ Account {acc_number} created! PIN: 1234")

def deposit(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    try:
        amount = float(input("Deposit amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        account['balance'] += amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Deposit", amount, account['balance'])
        print(f"✅ Deposited ₹{amount:.2f}")
        print(f"💰 New balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def withdraw(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    try:
        amount = float(input("Withdraw amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        if amount > account['balance']:
            print(f"❌ Insufficient! Available: ₹{account['balance']:.2f}")
            return
        
        account['balance'] -= amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Withdrawal", amount, account['balance'])
        print(f"✅ Withdrew ₹{amount:.2f}")
        print(f"💰 Remaining: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def check_balance(accounts):
    account = authenticate(accounts)
    if account:
        print(f"\n💰 Balance: ₹{account['balance']:.2f}")

def mini_statement(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    print(f"\n--- Mini Statement for Account {account['account_number']} ---")
    
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found!")
        return
    
    with open(TRANSACTIONS_FILE, 'r') as f:
        lines = f.readlines()
    
    acc_trans = [line for line in lines if f"Acc: {account['account_number']}" in line]
    
    if not acc_trans:
        print("No transactions for this account.")
        return
    
    for trans in acc_trans[-5:]:
        print(trans.strip())

def display_menu():
    print("\n" + "="*45)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Mini Statement")
    print("6. Exit")

def main():
    accounts = load_accounts()
    
    while True:
        display_menu()
        choice = input("Choice: ")
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            mini_statement(accounts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid!")
        
        input("\nPress Enter...")

if __name__ == "__main__":
    main()
    