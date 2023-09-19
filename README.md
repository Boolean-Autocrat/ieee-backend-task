This repo contains the solutions for the IEEE Backend Task by Suyash Handa.

# Details for the Bankings System (Q6)

The program contains several features releated to a standard backing system. There is requisite error handling, validation and input sanitization.

## Features

- Creating a new account
- Depositing money
- Withdrawing money
- Viewing the transaction history
- Viewing the account details
- Updating the account details
- Deleting/closing the account
- Searching for an account by name

## How to run

- Clone the repo
- Run the following commands

```

cd q6_banking_system
python main.py

```

- The program uses a sqlite database to store the data. The database is created in the same directory as the main.py file.
- The program also only uses the standard library, so no need to install any external packages.

## Folder Structure

The folder structure for the banking system is as follows:

```
q6_banking_system
├── main.py
├── AccountClass.py
├── WelcomeText.py
```
