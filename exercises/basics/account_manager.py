# Implement a simple bank account management system using functions and loops.
# The program should allow the user to:

# Create a new account
# Deposit money into the account
# Withdraw money from the account (ensure balance cannot go below zero)
# Check the current balance
# Exit the program

accounts = {}


def createAccount(account_number):
    if account_number in accounts:
        print("\nThis account number is already in use, create another one.\n")
    else:
        accounts[account_number] = 0
        print("\nAccount created successfully!\n")


def deposit(account_number, deposit_amount):
    if account_number in accounts:
        accounts[account_number] += deposit_amount
        print("\nThe deposit was successfull.\n")
    else:
        print("\nThis account does not exists.\n")


def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            print("Transaction successfull.")
            print("Amount withdrawed: ", amount)
            print("New account balance: ", accounts[account_number], "\n")
        else:
            print("\nInsufficient funds to complete transaction.\n")
    else:
        print("\nInvalid account number.\n")


def checkBalance(account_number):
    if account_number in accounts:
        print(f"Account {account_number} balance: {accounts[account_number]}\n")
    else:
        print("Invalid account number.")


def main():

    while True:
        print("-------- Welcome to FriendlyBank ---------")
        print("Enter 1 to create an account.")
        print("Enter 2 to deposit to your account.")
        print("Enter 3 to withdraw funds from your account.")
        print("Enter 4 to check your account balance.")
        print("Enter 5 to exit program.")

        option = int(input("\nPlease enter your choice: "))

        if option == 1:
            account_number = input("Please enter the new account number: ")
            createAccount(account_number)

        elif option == 2:
            account_number = input("Please enter the account number to deposit: ")
            deposit_amount = float(input("Please enter deposit amount: "))
            deposit(account_number, deposit_amount)

        elif option == 3:
            account_number = input("Please enter the account number to withdraw from: ")
            amount = float(input("Please enter amount to withdraw: "))
            withdraw(account_number, amount)

        elif option == 4:
            account_number = input("Pealse enter your account number: ")
            checkBalance(account_number)

        elif option == 5:
            print("Exiting program...")
            break

        else:
            print("\nPlease enter a valid option.\n")


if __name__ == "__main__":
    main()
