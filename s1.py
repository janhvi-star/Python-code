class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        if account.account_number not in self.accounts:
            self.accounts[account.account_number] = account
            print(f"Account {account.account_number} added for {self.name}.")
        else:
            print("Account already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added to the bank.")
        else:
            print("Customer already exists.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def list_customers(self):
        print("Bank Customers:")
        for customer_id, customer in self.customers.items():
            print(f"ID: {customer_id}, Name: {customer.name}")


# Example Usage
if __name__ == "__main__":
    # Create a bank
    my_bank = Bank("My Bank")

    # Create customers
   
