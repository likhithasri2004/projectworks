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