class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than zero."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Amount must be greater than zero."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    account = BankAccount("123456789", "John Doe", 1000.0)

    # Deposit money
    print(account.deposit(500))  # Deposited $500. New balance: $1500.0

    # Withdraw money
    print(account.withdraw(200))  # Withdrew $200. New balance: $1300.0

    # Display account balance
    print(account.display_balance())  # Account balance for John Doe: $1300.