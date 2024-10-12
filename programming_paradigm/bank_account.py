class BankAccount:
    """Simulates banking operations like withdrawals, deposits and balance checking"""
    
    def __init__(self, bank_balance: float = 0) -> None:
        """Initializes instances of the bank account. The balance at the creating of account is 0.
        Default name is assigned John-Doe"""
        # self.name_of_account = name_of_account  # Stores the name of the account holder
        self.__account_balance = bank_balance  # Initializes account balance, private to the class
    
    def deposit(self, amount: float):
        """Receives amount to be deposited by the user of the account"""

        if amount >= 0:
            self.__account_balance += amount  # Increases account balance if valid
            # print(f'Deposited: ${self.__account_balance}'
            return True
        elif amount < 0:
            # print(f'Error, the amount ${amount:.2f} is invalid.') # Rejects negative deposit amounts
            return False
        else:
            return f'Invalid Input, try again.'

    
    def withdraw(self, amount: float):
        """Withdraws amount from balance and updates current balance"""

        if 0 < amount <= self.__account_balance:  #and amount > 0:
            self.__account_balance -= amount  # Deducts the withdrawal amount from balance
            # print(f'Withdrew: ${self.__account_balance:.2f}')
            return True  # Confirms successful withdrawal 
        else: 
            return False  # Prevents withdrawal if balance is insufficient
        # elif amount < 0:
        #     print(f'Sorry cannot withdraw negative amount!')
        #     return False
        # else:
        #     return f'Invalid Input.'
        
    
    def display_balance(self):
        """Displays bank Balance"""
        print(f'Current Balance: ${self.__account_balance:.2f}')
        # return f'Current Balance: ${self.__account_balance:.2f}'  # Returns formatted b
