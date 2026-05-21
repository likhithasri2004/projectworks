# main_v1.py - Basic menu system with loops

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