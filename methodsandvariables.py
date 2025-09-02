class BankAccount:
    bank_name = "National Bank"     # Class Variable 
    
    def __init__(self, account_no, holder_name, balance):    # Instance Variables 
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance
    
    # Instance Method
    def deposit(self, amount):
        transaction_type = "Deposit"
        self.balance += amount
        print(f"{transaction_type} Successful! New Balance: {self.balance}")
    
    # Instance Method
    def withdraw(self, amount):
        transaction_type = "Withdrawal"
        if self.balance >= amount:
            self.balance -= amount
            print(f"{transaction_type} Successful! Remaining Balance: {self.balance}")
        else:
            print("Insufficient Funds!")
    
    # Class Method
    @classmethod
    def change_bank(cls, new_bank_name):
        cls.bank_name = new_bank_name
    
    # Static Method
    @staticmethod
    def bank_rules():
        print("Bank Rules: Maintain minimum balance of 1000. Interest is credited monthly.")


# Creating Objects
acc1 = BankAccount(1001, "Naina", 5000)
acc2 = BankAccount(1002, "Meera", 2000)

# Using Instance Methods
acc1.deposit(2000)
acc2.withdraw(1000)

# Accessing Class Variable
print("Bank Name:", BankAccount.bank_name)

# Using Class Method
BankAccount.change_bank("Global Trust Bank")
print("Updated Bank Name:", BankAccount.bank_name)

# Using Static Method
BankAccount.bank_rules()
