from account import accounts
from deposit import deposit
from withdraw import withdraw
from statement import show_statement
from utils import validate_user

# Login
user_id = input("Enter your Account ID: ")
pin = input("Enter your PIN: ")

if not validate_user(user_id, pin):
    print("Invalid ID or PIN!")
    exit()

print(f"Welcome {accounts[user_id]['name']} 👋")

def display_balance():
    print("Current Balance:", accounts[user_id]["balance"])

# ATM Menu
while True:
    print("\n--- ATM Menu ---")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        deposit(user_id)
    elif choice == "3":
        withdraw(user_id)
    elif choice == "4":
        show_statement(user_id)
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice!")
        
