# Create Bank Account class Object
class Account:

    # Initialize the account
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())


my_account = Account("PythonBasics/Object_Oriented_Programming/bank_account/balance.txt")
print(my_account.balance)
