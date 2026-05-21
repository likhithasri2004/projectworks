# BANK MANAGEMENT SYSTEM - COMPLETE FINAL VERSION (Windows Compatible)
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
    log = f"{timestamp} | Acc: {acc_number} | {trans_type}: Rs.{amount} | Balance: Rs.{balance}\n"
    with open(TRANSACTIONS_FILE, 'a', encoding='utf-8') as f:
        f.write(log)

def generate_acc_number(accounts):
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def authenticate(accounts):
    print("\n--- Login Required ---")
    acc_num = input("Enter Account Number: ").strip()
    
    if acc_num not in accounts:
        print("X Account not found!")
        return None
    
    pin = getpass("Enter PIN: ").strip()
    
    if accounts[acc_num]['pin'] == pin:
        print(f" Welcome back, {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("X Wrong PIN!")
        return None

def create_account(accounts):
    print("\n" + "="*50)
    print("        CREATE NEW ACCOUNT")
    print("="*50)
    
    name = input("Enter Account Holder Name: ").strip().title()
    if not name:
        print("X Name cannot be empty!")
        return
    
    mobile = input("Enter Mobile Number (10 digits): ").strip()
    if not validate_mobile(mobile):
        print("X Invalid mobile number! Must be 10 digits.")
        return
    
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
    
    try:
        deposit = float(input("Enter Initial Deposit (Min Rs.500): "))
        if deposit < 500:
            print("X Minimum initial deposit is Rs.500!")
            return
    except ValueError:
        print("X Invalid amount! Please enter a number.")
        return
    
    acc_number = generate_acc_number(accounts)
    
    accounts[str(acc_number)] = {
        'account_number': acc_number,
        'name': name,
        'mobile': mobile,
        'account_type': account_type,
        'balance': deposit,
        'pin': '1234'
    }
    
    save_accounts(accounts)
    log_transaction(acc_number, "Account Created", deposit, deposit)
    
    print("\n" + "="*50)
    print(" ACCOUNT CREATED SUCCESSFULLY!")
    print(f" Account Number : {acc_number}")
    print(f" Account Type   : {account_type}")
    print(f" Holder Name    : {name}")
    print(f" Default PIN    : 1234")
    print("="*50)

def view_account_details(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
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
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Deposit Money ---")
    try:
        amount = float(input("Enter amount to deposit: Rs."))
        if amount <= 0:
            print("X Amount must be positive!")
            return
        
        account['balance'] += amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Deposit", amount, account['balance'])
        
        print(f"\n Deposited Rs.{amount:.2f} successfully!")
        print(f" New Balance: Rs.{account['balance']:.2f}")
    except ValueError:
        print("X Invalid amount!")

def withdraw_amount(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Withdraw Money ---")
    try:
        amount = float(input("Enter amount to withdraw: Rs."))
        if amount <= 0:
            print("X Amount must be positive!")
            return
        if amount > account['balance']:
            print(f"X Insufficient balance! Available: Rs.{account['balance']:.2f}")
            return
        if amount > 20000:
            print("X Daily withdrawal limit is Rs.20,000!")
            return
        
        account['balance'] -= amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Withdrawal", amount, account['balance'])
        
        print(f"\n Withdrawn Rs.{amount:.2f} successfully!")
        print(f" Remaining Balance: Rs.{account['balance']:.2f}")
    except ValueError:
        print("X Invalid amount!")

def check_balance(accounts):
    account = authenticate(accounts)
    if account:
        print("\n" + "="*40)
        print(f" Current Balance: Rs.{account['balance']:.2f}")
        print("="*40)

def transfer_money(accounts):
    sender = authenticate(accounts)
    if not sender:
        return
    
    print("\n--- Transfer Money ---")
    receiver_acc = input("Enter receiver's account number: ").strip()
    
    if receiver_acc not in accounts:
        print("X Receiver account not found!")
        return
    
    if receiver_acc == str(sender['account_number']):
        print("X Cannot transfer to your own account!")
        return
    
    receiver = accounts[receiver_acc]
    
    try:
        amount = float(input(f"Enter amount to transfer to {receiver['name']}: Rs."))
        if amount <= 0:
            print("X Amount must be positive!")
            return
        if amount > sender['balance']:
            print(f"X Insufficient balance! Available: Rs.{sender['balance']:.2f}")
            return
        
        sender['balance'] -= amount
        receiver['balance'] += amount
        
        save_accounts(accounts)
        log_transaction(sender['account_number'], f"Transfer to {receiver_acc}", amount, sender['balance'])
        log_transaction(receiver['account_number'], f"Transfer from {sender['account_number']}", amount, receiver['balance'])
        
        print(f"\n Transferred Rs.{amount:.2f} to {receiver['name']} successfully!")
        print(f" Your new balance: Rs.{sender['balance']:.2f}")
    except ValueError:
        print("X Invalid amount!")

def mini_statement(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n" + "="*55)
    print(f"     MINI STATEMENT - Account: {account['account_number']}")
    print("="*55)
    
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found!")
        return
    
    with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    acc_trans = [line for line in lines if f"Acc: {account['account_number']}" in line]
    
    if not acc_trans:
        print("No transaction history found for this account.")
        return
    
    print("\nRecent Transactions:\n")
    for trans in acc_trans[-5:]:
        print(trans.strip())
    print("="*55)

def change_pin(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Change PIN ---")
    new_pin = getpass("Enter new 4-digit PIN: ").strip()
    
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("X PIN must be exactly 4 digits!")
        return
    
    confirm_pin = getpass("Confirm new PIN: ").strip()
    
    if new_pin != confirm_pin:
        print("X PINs do not match!")
        return
    
    account['pin'] = new_pin
    save_accounts(accounts)
    print(" PIN changed successfully!")

def delete_account(accounts):
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n WARNING: This action is irreversible!")
    confirm = input(f"Are you sure you want to delete account {account['account_number']}? (yes/no): ").lower()
    
    if confirm == 'yes':
        del accounts[str(account['account_number'])]
        save_accounts(accounts)
        log_transaction(account['account_number'], "Account Deleted", 0, 0)
        print(" Account deleted successfully!")
    else:
        print("X Deletion cancelled.")

def display_menu():
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
    accounts = load_accounts()
    
    print("\n WELCOME TO BANK MANAGEMENT SYSTEM")
    print("Your Trusted Banking Partner")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ").strip()
        
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
            print("\n Thank you for using Bank Management System!")
            print("Have a great day!")
            break
        else:
            print("X Invalid choice! Please enter a number between 1 and 10.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
