# BANK MANAGEMENT SYSTEM - COMPLETE FINAL VERSION
# All features working: Create, View, Deposit, Withdraw, Transfer, 
# Mini Statement, Change PIN, Delete Account, File Handling

import json
import os
from getpass import getpass
from datetime import datetime

# ============================================
# FILE HANDLING FUNCTIONS
# ============================================

ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

def load_accounts():
    """Load accounts from JSON file"""
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return {}

def save_accounts(accounts):
    """Save accounts to JSON file"""
    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def log_transaction(acc_number, trans_type, amount, balance):
    """Log each transaction to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{timestamp} | Acc: {acc_number} | {trans_type}: ₹{amount} | Balance: ₹{balance}\n"
    with open(TRANSACTIONS_FILE, 'a') as f:
        f.write(log)

# ============================================
# HELPER FUNCTIONS
# ============================================

def generate_acc_number(accounts):
    """Generate unique account number"""
    if not accounts:
        return 1001
    return max(int(k) for k in accounts.keys()) + 1

def validate_mobile(mobile):
    """Validate 10-digit mobile number"""
    return mobile.isdigit() and len(mobile) == 10

def authenticate(accounts):
    """PIN-based authentication"""
    print("\n--- Login Required ---")
    acc_num = input("Enter Account Number: ").strip()
    
    if acc_num not in accounts:
        print("❌ Account not found!")
        return None
    
    pin = getpass("Enter PIN: ").strip()
    
    if accounts[acc_num]['pin'] == pin:
        print(f"✅ Welcome back, {accounts[acc_num]['name']}!")
        return accounts[acc_num]
    else:
        print("❌ Wrong PIN!")
        return None

# ============================================
# CORE BANKING FUNCTIONS
# ============================================

def create_account(accounts):
    """Create a new bank account"""
    print("\n" + "="*40)
    print("        CREATE NEW ACCOUNT")
    print("="*40)
    
    name = input("Enter Account Holder Name: ").strip().title()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    mobile = input("Enter Mobile Number (10 digits): ").strip()
    if not validate_mobile(mobile):
        print("❌ Invalid mobile number! Must be 10 digits.")
        return
    
    try:
        deposit = float(input("Enter Initial Deposit (Min ₹500): "))
        if deposit < 500:
            print("❌ Minimum initial deposit is ₹500!")
            return
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
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
    
    print("\n" + "="*40)
    print("✅ ACCOUNT CREATED SUCCESSFULLY!")
    print(f"📌 Account Number: {acc_number}")
    print(f"🔐 Default PIN: 1234")
    print("="*40)

def view_account_details(accounts):
    """View details of a specific account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n" + "="*50)
    print("              ACCOUNT DETAILS")
    print("="*50)
    print(f"Account Number    : {account['account_number']}")
    print(f"Holder Name       : {account['name']}")
    print(f"Mobile Number     : {account['mobile']}")
    print(f"Current Balance   : ₹{account['balance']:.2f}")
    print("="*50)

def deposit_amount(accounts):
    """Deposit money into account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Deposit Money ---")
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        account['balance'] += amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Deposit", amount, account['balance'])
        
        print(f"\n✅ Deposited ₹{amount:.2f} successfully!")
        print(f"💰 New Balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def withdraw_amount(accounts):
    """Withdraw money from account"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Withdraw Money ---")
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        if amount > account['balance']:
            print(f"❌ Insufficient balance! Available: ₹{account['balance']:.2f}")
            return
        if amount > 20000:
            print("⚠️ Daily withdrawal limit is ₹20,000!")
            return
        
        account['balance'] -= amount
        save_accounts(accounts)
        log_transaction(account['account_number'], "Withdrawal", amount, account['balance'])
        
        print(f"\n✅ Withdrawn ₹{amount:.2f} successfully!")
        print(f"💰 Remaining Balance: ₹{account['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def check_balance(accounts):
    """Check account balance"""
    account = authenticate(accounts)
    if account:
        print("\n" + "="*40)
        print(f"💰 Current Balance: ₹{account['balance']:.2f}")
        print("="*40)

def transfer_money(accounts):
    """Transfer money between two accounts"""
    sender = authenticate(accounts)
    if not sender:
        return
    
    print("\n--- Transfer Money ---")
    receiver_acc = input("Enter receiver's account number: ").strip()
    
    if receiver_acc not in accounts:
        print("❌ Receiver account not found!")
        return
    
    if receiver_acc == str(sender['account_number']):
        print("❌ Cannot transfer to your own account!")
        return
    
    receiver = accounts[receiver_acc]
    
    try:
        amount = float(input(f"Enter amount to transfer to {receiver['name']}: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        if amount > sender['balance']:
            print(f"❌ Insufficient balance! Available: ₹{sender['balance']:.2f}")
            return
        
        # Process transfer
        sender['balance'] -= amount
        receiver['balance'] += amount
        
        save_accounts(accounts)
        log_transaction(sender['account_number'], f"Transfer to {receiver_acc}", amount, sender['balance'])
        log_transaction(receiver['account_number'], f"Transfer from {sender['account_number']}", amount, receiver['balance'])
        
        print(f"\n✅ Transferred ₹{amount:.2f} to {receiver['name']} successfully!")
        print(f"💰 Your new balance: ₹{sender['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount!")

def mini_statement(accounts):
    """Show last 5 transactions"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n" + "="*50)
    print(f"     MINI STATEMENT - Account: {account['account_number']}")
    print("="*50)
    
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions found!")
        return
    
    with open(TRANSACTIONS_FILE, 'r') as f:
        lines = f.readlines()
    
    # Filter transactions for this account
    acc_trans = [line for line in lines if f"Acc: {account['account_number']}" in line]
    
    if not acc_trans:
        print("No transaction history found for this account.")
        return
    
    # Show last 5 transactions (or fewer if less exist)
    for trans in acc_trans[-5:]:
        print(trans.strip())
    print("="*50)

def change_pin(accounts):
    """Change account PIN"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n--- Change PIN ---")
    new_pin = getpass("Enter new 4-digit PIN: ").strip()
    
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("❌ PIN must be exactly 4 digits!")
        return
    
    confirm_pin = getpass("Confirm new PIN: ").strip()
    
    if new_pin != confirm_pin:
        print("❌ PINs do not match!")
        return
    
    account['pin'] = new_pin
    save_accounts(accounts)
    print("✅ PIN changed successfully!")

def delete_account(accounts):
    """Delete an account permanently"""
    account = authenticate(accounts)
    if not account:
        return
    
    print("\n⚠️  WARNING: This action is irreversible!")
    confirm = input(f"Are you sure you want to delete account {account['account_number']}? (yes/no): ").lower()
    
    if confirm == 'yes':
        del accounts[str(account['account_number'])]
        save_accounts(accounts)
        log_transaction(account['account_number'], "Account Deleted", 0, 0)
        print("✅ Account deleted successfully!")
    else:
        print("❌ Deletion cancelled.")

# ============================================
# MENU SYSTEM
# ============================================

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("        🏦 BANK MANAGEMENT SYSTEM 🏦")
    print("="*50)
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
    print("="*50)

def main():
    """Main program loop"""
    accounts = load_accounts()
    
    print("\n🌟 WELCOME TO BANK MANAGEMENT SYSTEM 🌟")
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
            print("\n👋 Thank you for using Bank Management System!")
            print("Have a great day! 💰")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 10.")
        
        input("\nPress Enter to continue...")

# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    main()
