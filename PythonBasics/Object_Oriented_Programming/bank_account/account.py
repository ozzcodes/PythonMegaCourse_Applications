# Create Bank Account class Object
class Account:

    # Initialize the account
    def __init__(self, filepath):
        # Create local variable to access file path for later use
        """
        Args:
            filepath:
        """
        self.path = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    # Create another function for use in class
    def withdraw(self, amount):
        """
        Args:
            amount:
        """
        self.balance = self.balance - amount

    # Create deposit function and update account balance
    def deposit(self, amount):
        """
        Args:
            amount:
        """
        self.balance = self.balance + amount

    # Create a function to save the balance
    def update_balance(self):
        with(open(self.path, 'w')) as file:
            file.write(str(self.balance))


my_account = Account('balance.txt')

'''
Examples to use the bank account with Account class
'''


# my_account.withdraw(900)
# print(my_account.balance)
# my_account.update_balance()
# print(my_account.balance)
# my_account.deposit(1250)
# print(my_account.balance)


# Create a Second, sub-class using INHERITANCE
class Checking(Account):

    def __init__(self, filepath, fee):
        """
        Args:
            filepath:
            fee:
        """
        Account.__init__(self, filepath)
        self.fee = fee

    # Create a transfer function
    def transfer(self, amount):
        """
        Args:
            amount:
        """
        self.balance = self.balance - amount - self.fee


checking = Checking('balance.txt', 3.50)

'''
Examples to use the bank account with Account class
'''

checking.deposit(120.68)
print(checking.balance)
checking.transfer(355.87)
print(checking.balance)
checking.update_balance()
