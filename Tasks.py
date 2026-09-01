
from storage import get_bank_data, bank_database
class BankAccount:

    bank_name = "Linear Finance"
    no_of_accounts = 0
    total_bank_balance = 0

    @classmethod
    def show_bank_details(cls):
        print(f"\n\033[45m{cls.bank_name}\033[0m")
        print(f"\n\033[35mNumber of Accounts:{cls.no_of_accounts}\033[0m")
        print(f"\n\033[35mTotal Bank Balance:{cls.total_bank_balance}\033[0m")
        return classmethod



    def __init__(self, name, balance,number):
        self.holder = name
        self.account_number= number
        self.balance = balance
        BankAccount.no_of_accounts += 1


    def withdraw(self, amount):
        self.balance -= amount
        BankAccount.total_bank_balance -= amount

    def deposit(self, amount):
        self.balance += amount
        BankAccount.total_bank_balance += amount

def valid_number(prompt:str)->int:
    while True:
        number=int(input(prompt))
        if 0<=number<=10000:
            return number
        else:
            print("Please enter a number between 0 and 10000")

def valid_amount(prompt:str)->float:
    while True:
        number=float(input(prompt))
        if 0<=number<=1000000:
            return number
        else:
            print("Please enter a number between 0 and 1000000")
def create_bank_account():
    while True:
        account_holder=input("Please enter your name: ").title()
        balance=valid_amount("Please enter your balance: ")
        number=valid_number("Please enter your account number: ")

        bank_database.append(BankAccount(account_holder,balance,number))

        end_loop= input("Would you like to add more accounts? [y/n]")
        if end_loop=="n":
            print("Yay, Your account has been created!")
            break
        else:
            continue
    get_bank_data()
    return bank_database

def view_account():
    account_lookup=valid_amount("Please enter your account number: ")
    for account in bank_database:
        if account.account_number==account_lookup:
            print(f"Account holder: {account.holder}\nAccount number: {account.account_number}\nBalance: {account.balance}")
            return account
    print("Account not found")
    return None

def deposit_money():
    account_holder = view_account()
    if account_holder:
        while True:
            deposit_amount=valid_amount("Please enter your deposit amount: ")
            account_holder.deposit(deposit_amount)
            print(f"Your deposit amount of {deposit_amount} has been added to your account")

            end_deposits = input("Would you like to add more deposits? [y/n]")
            if end_deposits == "n":
                print("Yay, Your deposit has been added!")
                break
            else:
                continue
    else:
        print("Account not found")
    get_bank_data()

def withdraw_money():
    account_holder=view_account()
    if account_holder:
        while True:
            withdraw_amount=valid_amount("Please enter your withdraw amount: ")
            account_holder.withdraw(withdraw_amount)
            print(f"An amount of {withdraw_amount} has been withdrawn to your account")

            end_deposits = input("Would you like to withdraw more money? [y/n]").lower()
            if end_deposits == "n":
                print("Yay, Your money should be with you any moment from now!")
                break
            else:
                continue
    else:
        print("Account not found")
    get_bank_data()

def check_balance():
    account_holder=view_account()
    while True:
        if account_holder:
            print(f"Total Balance: {account_holder.balance}")
            break
        else:
            print("Account not found")
            break
def exit_program():
    print(f"Thanks for banking with{BankAccount.bank_name}")
    exit()
