from account import accounts

def validate_user(user_id, pin):
    return user_id in accounts and accounts[user_id]["pin"] == pin

def get_amount():
    try:
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("Amount should be positive!")
            return None
        return amount
    except:
        print("Invalid input!")
        return None
