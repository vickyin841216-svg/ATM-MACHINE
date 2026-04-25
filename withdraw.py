from account import accounts
from utils import get_amount

def withdraw(user_id):
    amount = get_amount()
    if amount:
        if amount <= accounts[user_id]["balance"]:
            accounts[user_id]["balance"] -= amount
            accounts[user_id]["transactions"].append(f"Withdrawn: {amount}")
            print("Please collect your cash.")
        else:
            print("gareeb hai!")
            
