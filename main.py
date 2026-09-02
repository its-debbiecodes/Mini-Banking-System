from Tasks import create_bank_account,view_account,withdraw_money,deposit_money,check_balance,exit_program,BankAccount
title= "===== MINI BANK =====".upper().center(100)
options=[
    "Add Account (press a)",
    "View Account (press v)",
    "Deposit Money (press d)",
    "Withdraw Money (press w)",
    "View Balance (press v)",
    "Exit (press e)"
]
def main():
    load_bank_data()
    BankAccount.show_bank_details()
    while True:
        print(f"\n\033[35m{title}\033[0m\n")
        print(f"\033[32m{"-" * 50}\033[0m")
        for index,option in enumerate(options,start=1):
            print(f"\n\033[32m{index}. {option:<20}\033[0m")
        print(f"\033[32m{"-" * 50}\033[0m")

        user_choice = input("\n\033[30mChoose an option:\033[0m ").lower()
        if user_choice == "a":
            create_bank_account()
        elif user_choice == "v":
            view_account()
        elif user_choice == "d":
            deposit_money()
        elif user_choice == "w":
            withdraw_money()
        elif user_choice == "v":
            check_balance()
        elif user_choice == "e":
            exit_program()

if __name__ == "__main__":
    main()