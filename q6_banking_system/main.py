from AccountClass import BankAccount


def menu():
    options = [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Account Summary",
        "Update Details",
        "Delete Account",
        "Exit",
    ]
    print("--------------------")
    for option in options:
        print(f"{options.index(option) + 1}. {option}")
    choice = int(input("Enter your choice: "))
    return choice


def main():
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
                account.update()
            elif option == 6:
                account.delete()
            elif option == 7:
                del account
                print("Thank you for using our services!")
                break
        except:
            print("Something went wrong! Please try again.")
            continue


if __name__ == "__main__":
    main()
