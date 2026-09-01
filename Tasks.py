
from storage import update_bank_data, bank_database
class BankAccount:

    bank_name = "Linear Finance"
    no_of_accounts = 0
    total_bank_balance = 0

    @classmethod
    def show_bank_details(cls):
        print(f"\n\033[45m{cls.bank_name}\033[0m")
        print(f"\n\033[35mNumber of Accounts:{cls.no_of_accounts}\033[0m")
        print(f"\n\033[35mTotal Bank Balance:{cls.total_bank_balance}\033[0m")


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
        account_holder=input("Please enter your name: ")
        balance=float(input("Please enter your balance: "))
        number=int(input("Please enter your account number: "))

        bank_database.append(BankAccount(account_holder,balance,number))

        end_loop= input("Would you like to add more accounts? [y/n]")
        if end_loop=="n":
            print("Yay, Your account has been created!")
            break
        else:
            continue
    update_bank_data(bank_database)
    return bank_database(BankAccount(account_holder,balance,number))

def view_account():
    account_lookup=input("Please enter your account number: ")#
    for account in bank_database:
        if account.account_number==account_lookup:
            print(f"Account holder: {account.holder}\nAccount number: {account.account_number}\nBalance: {account.balance}")
            return account
    print("Account not found")
    return None

def deposit_money():
    account_holder=view_account()
    if account_holder:
        deposit_amount=float(input("Please enter your deposit amount: "))
        account_holder.deposit(deposit_amount)
        print(f"Your deposit amount of {deposit_amount} has been added to your account")
        return deposit_amount
    else:
        print("Account not found")
        return None
get_bank_data()



