from AccountClass import BankAccount
from welcomeText import welcome_text


def menu():
    options = [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Account Summary",
        "Transaction History",
        "Update Details",
        "Close Account",
        "Search Account",
        "Exit",
    ]
    print("--------------------")
    for option in options:
        print(f"{options.index(option) + 1}. {option}")
    choice = int(input("Enter your choice: "))
    return choice


def main():
    print(welcome_text)
    print("Welcome to the Da Bank!\n(By Suyash Handa)")
    while True:
        try:
            try:
                option = menu()
            except:
                print("Invalid choice! Please try again.")
                continue
            account = BankAccount()
            if option == 1:
                account.create()
            elif option == 2:
                account.deposit()
            elif option == 3:
                account.withdraw()
            elif option == 4:
                account.summary()
            elif option == 5:
                account.displayTransactionHistory()
            elif option == 6:
                account.update()
            elif option == 7:
                account.closeAccount()
            elif option == 8:
                account.searchAccount()
            elif option == 9:
                del account
                print("Thank you for using our services @ Da Bank!")
                break
        except Exception as e:
            print("Something went wrong! Please try again.")
            print(e)
            continue


if __name__ == "__main__":
    main()
