#!/usr/bin/python3

class Checkbook:
    """
    Function description:
    Represents a simple checkbook that allows deposits, withdrawals,
    and balance inquiries.

    Parameters:
    None

    Returns:
    None
    """

    def __init__(self):
        """
        Function description:
        Initializes a new Checkbook instance with a zero balance.

        Parameters:
        None

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
        Adds a specified amount to the account balance.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
        Withdraws a specified amount from the account balance
        if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
        Displays the current account balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function description:
    Runs the main program loop, allowing the user to interact
    with the Checkbook through deposits, withdrawals, and balance checks.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()