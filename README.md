# ATM Machine (Python)

A simple and modular **ATM Simulation Project** built using Python.
This project demonstrates basic banking operations with **multiple users**, **PIN authentication**, and **transaction tracking**.

---

##  Features

*  User Login with Account ID & PIN
*  Display Account Balance
*  Deposit Money
*  Withdraw Money
*  Transaction Statement
*  Multiple User Support
*  Modular Code Structure (Separate Files)

---

##  Project Structure

```
ATM MACHINE/
│
├── account.py       # Stores user data (accounts, balance, PIN)
├── deposit.py       # Deposit functionality
├── withdraw.py      # Withdraw functionality
├── statement.py     # Transaction history
├── utils.py         # Helper functions (validation, input handling)
├── main.py          # Main program (menu + login system)
```

---

##  How It Works

1. User enters **Account ID** and **PIN**
2. System validates user credentials
3. After successful login, user can:

   * Check balance
   * Deposit money
   * Withdraw money
   * View transaction history
4. All transactions are stored in a list

---

##  How to Run

1. Make sure Python is installed
2. Clone the repository:

   ```
   git clone https://github.com/your-username/ATM-MACHINE.git
   ```
3. Navigate to the project folder:

   ```
   cd ATM-MACHINE
   ```
4. Run the program:

   ```
   python main.py
   ```

---

##  Sample Accounts

| Account ID | PIN  | Name   | Balance |
| ---------- | ---- | ------ | ------- |
| 1001       | 9798 | Vicky  | 10000   |
| 1002       | 9142 | Shobha | 15000   |
| 1003       | 8766 | Rahul  | 80000   |

---

##  Technologies Used

* Python
* Dictionary 
* Modular Programming

---

##  Future Improvements

*  Account lock after 3 wrong PIN attempts
*  Transaction with date & time
*  File/database storage (persistent data)

---

## Author

**Vicky Kumar**

---

## If you like this project

Give it a on GitHub and feel free to contribute!
