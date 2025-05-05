class BankAccount:
    account_counter = 1000  # Counter for account numbers

    def __init__(self, account_holder):
        """Initialize a bank account for the user."""
        self.account_holder = account_holder
        self.balance = 0.0
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

    def deposit(self, amount):
        """Deposit a certain amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        """Withdraw a certain amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds. Withdrawal cancelled.")
        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def display_balance(self):
        """Display the current balance of the account."""
        return (
            f"\n=== ACCOUNT INFO ===\n"
            f"Account Holder: {self.account_holder}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}"
        )

def menu(account):
    """Display the menu and handle user interaction with the bank account."""
    while True:
        print("\n==== BANK MENU ====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                result = account.deposit(amount)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                result = account.withdraw(amount)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "3":
            print(account.display_balance())

        elif choice == "4":
            print("Thanks for using the bank system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    try:
        name = input("Enter account holder's name: ").strip()
        if not name:
            raise ValueError("Account holder's name cannot be empty.")
        user_account = BankAccount(name)
        menu(user_account)
    except Exception as e:
        print(f"Program terminated due to error: {e}")
