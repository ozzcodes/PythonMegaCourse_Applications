# Create Bank Account class Object
class Account:

    # Initialize the account
    def __init__(self, filepath):
        # Create local variable to access file path for later use
        self.path = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    # Create another function for use in class
    def withdraw(self, amount):
        self.balance = self.balance - amount

    # Create deposit function and update account balance
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Create a function to save the balance
    def update_balance(self):
        with(open(self.path, 'w')) as file:
            file.write(str(self.balance))


my_account = Account('balance.txt')

my_account.withdraw(900)
print(my_account.balance)
my_account.update_balance()
print(my_account.balance)
my_account.deposit(1250)
print(my_account.balance)
