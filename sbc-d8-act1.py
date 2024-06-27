import os

# File to store user credentials (assuming plain text for simplicity)
credentials_file = "user_credentials.txt"

# Function to register a new user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if username already exists
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as file:
            for line in file:
                existing_username, _ = line.strip().split(',')
                if existing_username == username:
                    print("Username already exists. Please choose another.")
                    return

    # Append new user credentials to file
    with open(credentials_file, 'a') as file:
        file.write(f"{username},{password}\n")
        print("Registration successful.")

# Function to log in a user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if credentials match
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username and stored_password == password:
                    print("Login successful.")
                    return
        print("Invalid username or password.")

    else:
        print("No registered users.")

# Function to change password
def change_password():
    username = input("Enter username: ")
    old_password = input("Enter current password: ")
    new_password = input("Enter new password: ")

    # Check if username exists and update password
    if os.path.exists(credentials_file):
        updated_lines = []
        with open(credentials_file, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username:
                    if stored_password == old_password:
                        updated_lines.append(f"{username},{new_password}\n")
                        print("Password changed successfully.")
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
        
        with open(credentials_file, 'w') as file:
            file.writelines(updated_lines)
    
    else:
        print("No registered users.")

# Main menu function
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Example usage:
menu()
