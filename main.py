import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, initial_balance=0, withdrawal_limit=0):
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount and (self.withdrawal_limit == 0 or amount <= self.withdrawal_limit):
            self.balance -= amount
            return True
        else:
            return False

# Create the main application window
window = tk.Tk()
window.title("Banking App")

# Create the account objects
current_account = Account()
savings_account = Account(withdrawal_limit=500)  # Set withdrawal limit for savings account

# Function to handle the deposit button click
def deposit():
    amount = float(deposit_entry.get())
    if account_var.get() == "Current":
        current_account.deposit(amount)
        balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)
    else:
        savings_account.deposit(amount)
        balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)

# Function to handle the withdraw button click
def withdraw():
    amount = float(withdraw_entry.get())
    if account_var.get() == "Current":
        if current_account.withdraw(amount):
            balance_label.config(text="Current Account Balance: $%.2f" % current_account.balance)
        else:
            balance_label.config(text="Insufficient funds in Current Account")
    else:
        if savings_account.withdraw(amount):
            balance_label.config(text="Savings Account Balance: $%.2f" % savings_account.balance)
        else:
            balance_label.config(text="Insufficient funds in Savings Account")


# Run the main window event loop
window.mainloop()
