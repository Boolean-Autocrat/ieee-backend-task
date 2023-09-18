import sqlite3
import random


class BankAccount:
    def __init__(self):
        connection = sqlite3.connect("banking_system.db")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor
        query = "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, account_holder_name TEXT, account_balance INTEGER)"
        self.cursor.execute(query)

    def create(self):
        account_number = random.randint(1000000000, 9999999999)
        try:
            account_holder_name = input("Enter account holder name: ")
        except:
            print("Something went wrong! Please try again.")
            self.create()

        self.cursor.execute(
            "INSERT INTO accounts VALUES (?, ?, ?)",
            (account_number, account_holder_name, 0),
        )
        self.connection.commit()
        print("Account created successfully!\nAccount Number: ", account_number)

    def deposit(self):
        account_number = self.getAccount()
        account_balance = self.getBalance(account_number)

        try:
            dep_amount = int(input(f"Enter amount to deposit: {chr(8377)}"))
        except:
            print("Invalid amount! Please try again.")
            self.deposit()

        if dep_amount < 0:
            print("Negative amount! Please try again.")
            self.deposit()

        account_balance += dep_amount
        self.cursor.execute(
            "UPDATE accounts SET account_balance = ? WHERE account_number = ?",
            (account_balance, account_number),
        )
        self.connection.commit()
        print(
            f"Amount deposited successfully!\nAccount Balance: {chr(8377)}",
            account_balance,
        )

    def withdraw(self):
        account_number = self.getAccount()
        account_balance = self.getBalance(account_number)

        try:
            withdraw_amount = int(input(f"Enter amount to withdraw: {chr(8377)}"))
        except:
            print("Invalid amount! Please try again.")
            self.withdraw()

        if withdraw_amount < 0:
            print("Negative amount! Please try again.")
            self.withdraw()

        if withdraw_amount > account_balance:
            print("Insufficient balance!")
            self.withdraw()

        account_balance -= withdraw_amount
        self.cursor.execute(
            "UPDATE accounts SET account_balance = ? WHERE account_number = ?",
            (account_balance, account_number),
        )
        self.connection.commit()
        print(
            f"Amount withdrawn successfully!\nAccount Balance: {chr(8377)}",
            account_balance,
        )

    def summary(self):
        account_number = self.getAccount()
        account_balance = self.getBalance(account_number)

        self.cursor.execute(
            "SELECT account_holder_name FROM accounts WHERE account_number = ?",
            (account_number,),
        )
        self.connection.commit()
        account_holder_name = self.cursor.fetchone()[0]
        print("Account Summary: ")
        print("Account Holder Name: ", account_holder_name)
        print("Account Number: ", account_number)
        print(f"Account Balance: {chr(8377)}", account_balance)

    def update(self):
        account_number = self.getAccount()
        account_name = input("Enter new account holder name: ")
        self.cursor.execute(
            "UPDATE accounts SET account_holder_name = ? WHERE account_number = ?",
            (account_name, account_number),
        )
        self.connection.commit()
        print("Account updated successfully!")

    def delete(self):
        account_number = self.getAccount()
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (account_number,)
        )
        self.connection.commit()
        print("Account deleted successfully!")

    def getBalance(self, account_number):
        self.cursor.execute(
            "SELECT account_balance FROM accounts WHERE account_number = ?",
            (account_number,),
        )
        account_balance = self.cursor.fetchone()
        return account_balance[0]

    def getAccount(self):
        account_number = int(input("Enter account number: "))
        if self.getBalance(account_number) is None:
            print("Account does not exist! Please try again.")
            self.getAccount()
        return account_number

    def __del__(self):
        self.connection.close()
