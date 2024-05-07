class BankAccount:
    account_counter = 1000  

    def __init__(self, name, email, address, account_type):
        BankAccount.account_counter += 1
        self.account_number = str(BankAccount.account_counter)  
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0
        self.max_loan_count = 2

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        else:
            print("Withdrawal amount exceeded")
            return False

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient_account.name}")
            return True
        else:
            print("Insufficient funds to transfer")
            return False

    def take_loan(self, loan_amount):
        if self.loan_taken < self.max_loan_count:
            self.loan_taken += 1
            self.balance += loan_amount
            self.transaction_history.append(f"Took a loan of ${loan_amount}")
            return True
        else:
            print("You have already taken the maximum number of loans.")
            return False

class BankAdmin:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter user's name: ")
        email = input("Enter user's email address: ")
        address = input("Enter user's address: ")
        account_type = input("Enter account type (Savings/Current): ").capitalize()

        new_account = BankAccount(name, email, address, account_type)
        self.accounts.append(new_account)
        print(f"Account created successfully!\nYour Account Number is {new_account.account_number}")
        return new_account


    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} deleted successfully.")
                return True
        print("Account not found.")
        return False

    def list_accounts(self):
        print("Accounts:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}")

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)
        return total

    def total_loan_amount(self):
        total = sum(account.loan_taken for account in self.accounts)
        return total


def display_user_menu(user_account):
    print("\nUser Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. View Transaction History")
    print("6. Take Loan")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        user_account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        user_account.withdraw(amount)
    elif choice == '3':
        recipient_account_number = input("Enter recipient's account number: ")
        recipient_account = find_account_by_number(recipient_account_number)
        if recipient_account:
            amount = float(input("Enter transfer amount: "))
            user_account.transfer(amount, recipient_account)
        else:
            print("Recipient account not found.")
    elif choice == '4':
        print(f"Available Balance: ${user_account.balance}")
    elif choice == '5':
        print("Transaction History:")
        for transaction in user_account.transaction_history:
            print(transaction)
    elif choice == '6':
        loan_amount = float(input("Enter loan amount: "))
        user_account.take_loan(loan_amount)
    elif choice == '0':
        print("Exiting user menu...")
        return
    else:
        print("Invalid choice")

def find_account_by_number(account_number):
    for account in bank_admin.accounts:
        if account.account_number == account_number:
            return account
    return None


bank_admin = BankAdmin()

while True:
    print("\nWelcome to the Banking System")
    print("1. Admin Login")
    print("2. User Login")
    print("0. Exit")

    role_choice = input("Enter your role choice: ")

    if role_choice == '1':
        
        admin_password = input("Enter admin password: ")  
        if admin_password == "admin123":  
            print("Admin Login successful.")
            while True:
                print("\nAdmin Menu:")
                print("1. Create Account")
                print("2. Delete Account")
                print("3. List Accounts")
                print("4. Total Bank Balance")
                print("5. Total Loan Amount")
                print("0. Exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    new_account = bank_admin.create_account()
                elif admin_choice == '2':
                    account_number = input("Enter account number to delete: ")
                    bank_admin.delete_account(account_number)
                elif admin_choice == '3':
                    bank_admin.list_accounts()
                elif admin_choice == '4':
                    print(f"Total Bank Balance: ${bank_admin.total_balance()}")
                elif admin_choice == '5':
                    print(f"Total Loan Amount: ${bank_admin.total_loan_amount()}")
                elif admin_choice == '0':
                    print("Exiting admin menu...")
                    break
                else:
                    print("Invalid choice")

        else:
            print("Invalid admin password. Access denied.")

    elif role_choice == '2':
        
        account_number = input("Enter your account number: ")
        user_account = find_account_by_number(account_number)
        if user_account:
            print(f"Welcome, {user_account.name}!")
            while True:
                display_user_menu(user_account)
        else:
            print("Account not found. Please try again.")

    elif role_choice == '0':
        print("Exiting the Banking System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
