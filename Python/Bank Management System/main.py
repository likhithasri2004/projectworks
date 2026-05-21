# Bank Management System - My internship project
# Made by Likhitha Sri

import json
import os
from getpass import getpass
from datetime import datetime

# These are the files where I save everything
ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# ------------------------------------------------------
# Loading and saving data
# ------------------------------------------------------

def load_accounts():
    """Read all accounts from the file when program starts"""
    # If file doesn't exist yet, just return empty dictionary
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    
    with open(ACCOUNTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            # If file is corrupted or empty, start fresh
            return {}

def save_accounts(accounts):
    """Save all accounts to file after any change"""
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def log_transaction(acc_number, trans_type, amount, balance):
    """Keep a record of everything user does"""
    # Get current time for this transaction
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Make a log entry
    log = f"{timestamp} | Acc: {acc_number} | {trans_type}: Rs.{amount} | Balance: Rs.{balance}\n"
    
    # Add it to the transactions file
    with open(TRANSACTIONS_FILE, 'a', encoding='utf-8') as f:
        f.write(log)

# ------------------------------------------------------
# Small helper functions
# ------------------------------------------------------

def generate_acc_number(accounts):
    """Give a new account number - starts from 1001"""
    if not accounts:
        return 1001  # First account gets 1001
    
    # Find biggest number and add 1
    return max(int(k) for k in accounts.keys()) + 1

def validate_mobile(mobile):
    """Check if mobile number is exactly 10 digits"""
    return mobile.isdigit() and len(mobile) == 10

def authenticate(accounts):
    """Ask for account number and PIN, check if correct"""
    print("\n--- Login Required ---")
    
    acc_num = input("Enter Account Number: ").strip()
    
    # Does this account exist?
    if acc_num not in accounts:
        print("X Account not found!")
        return None
    
    # PIN is hidden while typing (getpass makes it invisible)
    pin = getpass("Enter PIN: ").strip()
    
    if accounts[acc_num]['pin'] == pin:
        print(f" Welcome back, {accounts[acc_num]['name']}!")
        return accounts[acc_num]  # Return the account details
    else:
        print("X Wrong PIN!")
        return None

# ------------------------------------------------------
# Main banking features
# ------------------------------------------------------

def create_account(accounts):
    """Let user open a new bank account"""
    print("\n" + "="*50)
    print("        CREATE NEW ACCOUNT")
    print("="*50)
    
    # Get name
    name = input("Enter Account Holder Name: ").strip().title()
    if not name:
        print("X Name cannot be empty!")
        return
    
    # Get mobile number and check it's 10 digits
    mobile = input("Enter Mobile Number (10 digits): ").strip()
    if not validate_mobile(mobile):
        print("X Invalid mobile number! Must be 10 digits.")
        return
    
    # Ask what type of account they want
    print("\nAccount Types:")
    print("1. Savings Account")
    print("2. Current Account")
    acc_type_choice = input("Choose account type (1/2): ").strip()
    
    if acc_type_choice == '1':
        account_type = "Savings"
    elif acc_type_choice == '2':
        account_type = "Current"
    else:
        print("X Invalid choice! Defaulting to Savings")
        account_type = "Savings"
    
    # Get initial deposit - minimum 500 rupees
    try:
        deposit = float(input("Enter Initial Deposit (Min Rs.500): "))
        if deposit < 500:
            print("X Minimum initial deposit is Rs.500!")
            return
    except ValueError:
        print("X Invalid amount! Please enter a number.")
        return
    
    # Generate new account number
    acc_number = generate_acc_number(accounts)
    
    # Store everything in a dictionary
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'account_type': account_type,
        'balance': deposit,
        'pin': '1234'  # Default PIN, they can change it later
    }
    
    # Save and log
    save_accounts(accounts)
    log_transaction(acc_number, "Account Created", deposit, deposit)
    
    # Tell user their account number
    print("\n" + "="*50)
    print(" ACCOUNT CREATED SUCCESSFULLY!")
    print(f" Account Number : {acc_number}")
    print(f" Account Type   : {account_type}")
    print(f" Holder Name    : {name}")
    print(f" Default PIN    : 1234")
    print("="*50)

def view_account_details(accounts):
    """Show all details of an account"""
    account = authenticate(accounts)  # First make sure it's the right person
    if not account:
        return
    
    # Print all account info
    print("\n" + "="*55)
    print("              ACCOUNT DETAILS")
    print("="*55)
    print(f"Account Number    : {account['account_number']}")
    print(f"Holder Name       : {account['name']}")
    print(f"Mobile Number     : {account['mobile']}")
    print(f"Account Type      : {account.get('account_type', 'Savings')}")
    print(f"Current Balance   : Rs.{account['balance']:.2f}")
    print("="*55)

def deposit_amount(accounts):
    """Add money to an account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Deposit Money ---")
    
    try:
        amount = float(input("Enter amount to deposit: Rs."))
        
        # Can't deposit negative or zero
        if amount <= 0:
            print("X Amount must be positive!")
            return
        
        # Add money to balance
        account['balance'] += amount
        
        # Save and log
        save_accounts(accounts)
        log_transaction(account['account_number'], "Deposit", amount, account['balance'])
        
        print(f"\n Deposited Rs.{amount:.2f} successfully!")
        print(f" New Balance: Rs.{account['balance']:.2f}")
        
    except ValueError:
        print("X Invalid amount!")

def withdraw_amount(accounts):
    """Take money out of an account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Withdraw Money ---")
    
    try:
        amount = float(input("Enter amount to withdraw: Rs."))
        
        if amount <= 0:
            print("X Amount must be positive!")
            return
        
        # Check if they have enough money
        if amount > account['balance']:
            print(f"X Insufficient balance! Available: Rs.{account['balance']:.2f}")
            return
        
        # Daily limit is 20,000
        if amount > 20000:
            print("X Daily withdrawal limit is Rs.20,000!")
            return
        
        # Subtract money from balance
        account['balance'] -= amount
        
        save_accounts(accounts)
        log_transaction(account['account_number'], "Withdrawal", amount, account['balance'])
        
        print(f"\n Withdrawn Rs.{amount:.2f} successfully!")
        print(f" Remaining Balance: Rs.{account['balance']:.2f}")
        
    except ValueError:
        print("X Invalid amount!")

def check_balance(accounts):
    """Just show how much money is in the account"""
    account = authenticate(accounts)
    if account:
        print("\n" + "="*40)
        print(f" Current Balance: Rs.{account['balance']:.2f}")
        print("="*40)

def transfer_money(accounts):
    """Send money from one account to another"""
    sender = authenticate(accounts)
    if not sender:
        return
    
    print("\n--- Transfer Money ---")
    
    # Who are we sending to?
    receiver_acc = input("Enter receiver's account number: ").strip()
    
    # Check if that account exists
    if receiver_acc not in accounts:
        print("X Receiver account not found!")
        return
    
    # Can't send to yourself
    if receiver_acc == str(sender['account_number']):
        print("X Cannot transfer to your own account!")
        return
    
    receiver = accounts[receiver_acc]
    
    try:
        amount = float(input(f"Enter amount to transfer to {receiver['name']}: Rs."))
        
        if amount <= 0:
            print("X Amount must be positive!")
            return
        
        # Check if sender has enough money
        if amount > sender['balance']:
            print(f"X Insufficient balance! Available: Rs.{sender['balance']:.2f}")
            return
        
        # Do the transfer
        sender['balance'] -= amount
        receiver['balance'] += amount
        
        save_accounts(accounts)
        
        # Log for both people
        log_transaction(sender['account_number'], f"Transfer to {receiver_acc}", amount, sender['balance'])
        log_transaction(receiver['account_number'], f"Transfer from {sender['account_number']}", amount, receiver['balance'])
        
        print(f"\n Transferred Rs.{amount:.2f} to {receiver['name']} successfully!")
        print(f" Your new balance: Rs.{sender['balance']:.2f}")
        
    except ValueError:
        print("X Invalid amount!")

def mini_statement(accounts):
    """Show last 5 transactions of an account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n" + "="*55)
    print(f"     MINI STATEMENT - Account: {account['account_number']}")
    print("="*55)
    
    # Check if we have any transactions recorded
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found!")
        return
    
    # Read all transactions
    with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Keep only transactions of this account
    acc_trans = [line for line in lines if f"Acc: {account['account_number']}" in line]
    
    if not acc_trans:
        print("No transaction history found for this account.")
        return
    
    # Show last 5 transactions only
    print("\nRecent Transactions:\n")
    for trans in acc_trans[-5:]:  # Last 5 items
        print(trans.strip())
    print("="*55)

def change_pin(accounts):
    """Let user change their 4-digit PIN"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Change PIN ---")
    
    new_pin = getpass("Enter new 4-digit PIN: ").strip()
    
    # Must be exactly 4 digits
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("X PIN must be exactly 4 digits!")
        return
    
    confirm_pin = getpass("Confirm new PIN: ").strip()
    
    if new_pin != confirm_pin:
        print("X PINs do not match!")
        return
    
    # Save the new PIN
    account['pin'] = new_pin
    save_accounts(accounts)
    print(" PIN changed successfully!")

def delete_account(accounts):
    """Completely remove an account"""
    account = authenticate(accounts)
    if not account:
        return
    
    # Warn them because this is permanent
    print("\n WARNING: This action is irreversible!")
    
    confirm = input(f"Are you sure you want to delete account {account['account_number']}? (yes/no): ").lower()
    
    if confirm == 'yes':
        # Remove from dictionary
        del accounts[str(account['account_number'])]
        
        save_accounts(accounts)
        log_transaction(account['account_number'], "Account Deleted", 0, 0)
        
        print(" Account deleted successfully!")
    else:
        print("X Deletion cancelled.")

# ------------------------------------------------------
# Menu and main program
# ------------------------------------------------------

def display_menu():
    """Show all options to user"""
    print("\n" + "="*55)
    print("        BANK MANAGEMENT SYSTEM")
    print("="*55)
    print("1.  Create Account")
    print("2.  View Account Details")
    print("3.  Deposit Amount")
    print("4.  Withdraw Amount")
    print("5.  Check Balance")
    print("6.  Transfer Money")
    print("7.  Mini Statement")
    print("8.  Change PIN")
    print("9.  Delete Account")
    print("10. Exit")
    print("="*55)

def main():
    """Where everything starts and runs"""
    # Load existing accounts when program opens
    accounts = load_accounts()
    
    print("\n WELCOME TO BANK MANAGEMENT SYSTEM")
    print("Your Trusted Banking Partner")
    
    # Keep showing menu until user chooses exit
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ").strip()
        
        # Call the right function based on user's choice
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            view_account_details(accounts)
        elif choice == '3':
            deposit_amount(accounts)
        elif choice == '4':
            withdraw_amount(accounts)
        elif choice == '5':
            check_balance(accounts)
        elif choice == '6':
            transfer_money(accounts)
        elif choice == '7':
            mini_statement(accounts)
        elif choice == '8':
            change_pin(accounts)
        elif choice == '9':
            delete_account(accounts)
        elif choice == '10':
            # Goodbye message
            print("\n Thank you for using Bank Management System!")
            print("Have a great day!")
            break
        else:
            print("X Invalid choice! Please enter a number between 1 and 10.")
        
        # Wait for user to press enter before showing menu again
        input("\nPress Enter to continue...")

# Start the program
if __name__ == "__main__":
    main()