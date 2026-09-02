import json
from Tasks import BankAccount
import Tasks
def load_bank_data():
    try:
        with open("bank_data.json", "r") as f:
            raw_data =json.load(f)
            Tasks.bank_database =[
                BankAccount(d["holder"], d["balance"], d["account_number"])
                for d in raw_data
            ]
            BankAccount.total_bank_balance =sum(a.balance for a in Tasks.bank_database)
    except FileNotFoundError:
        print("Bank data file not found, starting with empty database")
        Tasks.bank_database = []
    except json.decoder.JSONDecodeError:
        print("Warning: bank_data.json missing or corrupt. starting a new file")
        Tasks.bank_database = []


def save_bank_data():
    striped_bank_database = [account.__dict__ for account in Tasks.bank_database]
    with open("bank_data.json", "w") as file:
        json.dump(striped_bank_database, file, indent=4)