from account import accounts

def show_statement(user_id):
    print("\n--- Transaction Statement ---")
    if len(accounts[user_id]["transactions"]) == 0:
        print("No transactions yet.")
    else:
        for t in accounts[user_id]["transactions"]:
            print(t)
