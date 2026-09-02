from Tasks import create_bank_account,view_account,withdraw_money,deposit_money,check_balance,delete_account,exit_program,BankAccount
from storage import load_bank_data, save_bank_data
title= "===== MINI BANK =====".upper().center(100)
options=[
    "Add Account (press a)",
    "View Account (press v)",
    "Deposit Money (press d)",
    "Withdraw Money (press w)",
    "Check Balance (press v)",
    "delete Account (press q)",
    "Exit (press e)"
]
def main():
    load_bank_data()
    BankAccount.show_bank_details()
    print(f"\n\033[35m{title}\033[0m\n")
    while True:
        print(f"\033[32m{"-" * 50}\033[0m")
        for index,option in enumerate(options,start=1):
            print(f"\033[32m{index}. {option}\033[0m")
        print(f"\033[32m{"-" * 50}\033[0m")

        user_choice = input("\n\033[34mChoose an option:\033[0m ").lower()
        if user_choice == "a":
            create_bank_account()
            save_bank_data()
        elif user_choice == "v":
            view_account()
        elif user_choice == "d":
            deposit_money()
            save_bank_data()
        elif user_choice == "w":
            withdraw_money()
            save_bank_data()
        elif user_choice == "c":
            check_balance()
        elif user_choice == "q":
            delete_account()
            save_bank_data()
        elif user_choice == "e":
            exit_program()

if __name__ == "__main__":
    main()