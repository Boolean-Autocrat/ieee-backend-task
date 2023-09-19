import sqlite3
import random
import time
from datetime import datetime


class BankAccount:
    def __init__(self):
        connection = sqlite3.connect("banking_system.db")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor
        self.maxAttempts = 3
        query = "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, account_holder_name TEXT, account_balance INTEGER DEFAULT 0, account_type TEXT DEFAULT 'savings', transaction_history TEXT DEFAULT '[]', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        self.cursor.execute(query)

    def create(self):
        account_number = random.randint(1000000000, 9999999999)
        try:
            account_holder_name = input("Enter account holder name: ")
            account_holder_name = account_holder_name.strip().title()
            account_type = input("Enter account type (savings/current): ")
            account_type = account_type.strip().lower()
            if account_type not in ["savings", "current"]:
                print("Invalid account type! Please try again.")
                self.create()
        except:
            print("Something went wrong! Please try again.")
            self.create()

        self.cursor.execute(
            "INSERT INTO accounts (account_number, account_holder_name, account_type, created_at) VALUES (?, ?, ?, ?)",
            (
                account_number,
                account_holder_name,
                account_type,
                time.strftime("%d-%m-%Y %H:%M:%S"),
            ),
        )
        self.connection.commit()
        print()
        print("Account created successfully!\nAccount Number: ", account_number)

    def deposit(self):
        account_number, account_balance = self.getAccount()

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
        transaction_history = self.getTransactionHistory(account_number)
        transaction_history.append(
            f"{time.strftime('%d-%m-%Y %H:%M:%S')} - {dep_amount} deposited"
        )
        self.cursor.execute(
            "UPDATE accounts SET transaction_history = ? WHERE account_number = ?",
            (str(transaction_history), account_number),
        )
        self.connection.commit()
        print()
        print(
            f"Amount deposited successfully!\nAccount Balance: {chr(8377)}",
            account_balance,
        )

    def withdraw(self):
        account_number, account_balance = self.getAccount()

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
            return

        account_balance -= withdraw_amount
        self.cursor.execute(
            "UPDATE accounts SET account_balance = ? WHERE account_number = ?",
            (account_balance, account_number),
        )
        self.connection.commit()
        print()
        transaction_history = self.getTransactionHistory(account_number)
        transaction_history.append(
            f"{time.strftime('%d-%m-%Y %H:%M:%S')} - {withdraw_amount} withdrawn"
        )
        self.cursor.execute(
            "UPDATE accounts SET transaction_history = ? WHERE account_number = ?",
            (str(transaction_history), account_number),
        )
        self.connection.commit()
        print(
            f"Amount withdrawn successfully!\nAccount Balance: {chr(8377)}",
            account_balance,
        )

    def summary(self):
        account_number, account_balance = self.getAccount()

        self.cursor.execute(
            "SELECT account_holder_name, account_type, created_at FROM accounts WHERE account_number = ?",
            (account_number,),
        )
        self.connection.commit()
        account_details = self.cursor.fetchone()
        transaction_history = self.getTransactionHistory(account_number)
        time_str = (
            datetime.strptime(account_details[2], "%d-%m-%Y %H:%M:%S")
        ).strftime("%B %d, %Y %I:%M %p") + " IST"
        print()
        print("Account Summary: ")
        print("Account Holder Name: ", account_details[0])
        print("Account Type: ", account_details[1])
        print("Account Number: ", account_number)
        print(f"Account Balance: {chr(8377)}", account_balance)
        print("Created At: ", time_str)
        print("Transaction History: ")
        if len(transaction_history) == 0:
            print("No transactions yet!")
            return
        for transaction in transaction_history[::-1]:
            print(
                transaction.split(" - ")[0]
                + " - "
                + f"{chr(8377)}"
                + transaction.split(" - ")[1]
            )

    def update(self):
        account_number, _ = self.getAccount()
        account_name = input("Enter new account holder name: ")
        self.cursor.execute(
            "UPDATE accounts SET account_holder_name = ? WHERE account_number = ?",
            (account_name, account_number),
        )
        self.connection.commit()
        print()
        print("Account updated successfully!")

    def closeAccount(self):
        account_number, _ = self.getAccount()
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (account_number,)
        )
        self.connection.commit()
        print()
        print("Account closed successfully!")

    def searchAccount(self):
        account_name = input("Enter account holder name: ")
        account_name = account_name.strip()
        self.cursor.execute(
            "SELECT account_number, account_holder_name FROM accounts WHERE account_holder_name LIKE ?",
            ("%" + account_name + "%",),
        )
        accounts = self.cursor.fetchall()
        print()
        print("Search Results: ")
        if len(accounts) == 0:
            print("No accounts found!")
            return
        for account in accounts:
            print(f"{account[0]} - {account[1]}")

    def getBalance(self, account_number):
        self.cursor.execute(
            "SELECT account_balance FROM accounts WHERE account_number = ?",
            (account_number,),
        )
        account_balance = self.cursor.fetchone()
        return account_balance if account_balance is None else account_balance[0]

    def getAccount(self):
        account_number = int(input("Enter account number: "))
        balance = self.getBalance(account_number)
        if balance is None:
            print("Account does not exist! Please try again.")
            if self.maxAttempts > 1:
                self.maxAttempts -= 1
                self.getAccount()
            else:
                print("Too many attempts! Please try again later.")
                exit()
        return account_number, balance

    def getTransactionHistory(self, account_number):
        self.cursor.execute(
            "SELECT transaction_history FROM accounts WHERE account_number = ?",
            (account_number,),
        )
        transaction_history = self.cursor.fetchone()[0]
        transaction_history = eval(transaction_history)
        return transaction_history

    def displayTransactionHistory(self):
        account_number, _ = self.getAccount()
        transaction_history = self.getTransactionHistory(account_number)
        print()
        print("Transaction History: ")
        if len(transaction_history) == 0:
            print("No transactions yet!")
            return
        for transaction in transaction_history[::-1]:
            print(
                transaction.split(" - ")[0]
                + " - "
                + f"{chr(8377)}"
                + transaction.split(" - ")[1]
            )

    def __del__(self):
        self.connection.close()
