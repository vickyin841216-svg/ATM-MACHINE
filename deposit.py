from account import accounts
from utils import get_amount

def deposit(user_id):
    amount = get_amount()
    if amount:
        accounts[user_id]["balance"] += amount
        accounts[user_id]["transactions"].append(f"Deposited: {amount}")
        print("Amount deposited successfully maje karo!") 
        
