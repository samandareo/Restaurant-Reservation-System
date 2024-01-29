from Manager import main as manager_main
from Customer import main as customer_main
import os

def clear():
    if os.name == "nt":
        os.system("cls")

def main():
    while True:
        print("#"+"-#"*25)
        print("#                                                 #")
        print("#    Welcome to the Restaurant Management System   #")
        print("#                                                 #")
        print("#"+"-#"*25)
        print("\n[1] Manager Login")
        print("[2] Customer Login")
        print("[3] Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager_login()
        elif choice == '2':
            customer_login()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def manager_login():
    clear()
    manager_main()

def customer_login():
    clear()
    customer_main()

if __name__ == "__main__":
    main()
