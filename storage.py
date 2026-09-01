import json
bank_database= []
try:
    with open("bank_data.json", "r") as f:
        bank_database =json.load(f)
except FileNotFoundError:
    print("Bank data file not found, starting with empty database")
    bank_database = []
except json.decoder.JSONDecodeError:
    print("Warning: bank_data.json missing or corrupt. starting a new file")
    bank_database = []

def update_bank_data(striped_bank_database):
    with open("bank_data.json", "w") as file:
        json.dump(striped_bank_database, file, indent=4)
        return striped_bank_database

def get_bank_data():
    striped_bank_database = []
    for account in bank_database:
        striped_data=account.__dict__
        striped_bank_database.append(striped_data)
    update_bank_data(striped_bank_database)