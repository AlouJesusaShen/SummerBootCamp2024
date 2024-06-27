import os
from random import randint

data = {}

# Function to create a new user with a random ID and initial balance of 1000
def create_user():
    user_id = randint(1, 10000)
    while user_id in data:
        user_id = randint(1, 10000)
    data[user_id] = 1000
    print(f"User created successfully with ID: {user_id}")

# Function to check user balance
def check_balance(user_id):
    if user_id in data:
        print(f"User ID: {user_id}, Balance: {data[user_id]}")
    else:
        print("User ID does not exist")

# Function to delete a user
def delete_user(user_id):
    if user_id in data:
        del data[user_id]
        print(f"User ID: {user_id} deleted successfully")
    else:
        print("User ID does not exist")

# Function to deposit into user account
def deposit(user_id):
    if user_id in data:
        try:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                data[user_id] += amount
                print(f"Deposit of {amount} successful")
            else:
                print("Deposit amount must be greater than zero")
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
    else:
        print("User ID does not exist")

# Function to withdraw from user account
def withdraw(user_id):
    if user_id in data:
        try:
            amount = int(input("Enter withdrawal amount: "))
            if 0 < amount <= data[user_id]:
                data[user_id] -= amount
                print(f"Withdrawal of {amount} successful")
            else:
                print("Insufficient funds")
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
    else:
        print("User ID does not exist")

# Menu function
def menu():
    while True:
        print("\n===== WATSON EMPLOYEE BANK =====")
        print("1. Create User")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete User")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            create_user()
        elif choice == '2':
            user_id = int(input("Enter User ID: "))
            check_balance(user_id)
        elif choice == '3':
            user_id = int(input("Enter User ID: "))
            deposit(user_id)
        elif choice == '4':
            user_id = int(input("Enter User ID: "))
            withdraw(user_id)
        elif choice == '5':
            user_id = int(input("Enter User ID: "))
            delete_user(user_id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

menu()
