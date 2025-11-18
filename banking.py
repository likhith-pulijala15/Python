from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass


class BankAccount(Account):
    def __init__(self,account_no,name,balance=0):
        self.__account_no = account_no
        self.__name = name
        self.__balance = balance

    def get_account_no(self):
        return self.__account_no
    
    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance

    def set_name(self,new_name):
        self.__name = new_name

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} Deposited.\nBalance after deposit: {self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn.\nBalance after withdraw: {self.__balance}")
        else:
            print("Insufficient Balance")
 
    def details(self):
        print(f"\nAccount number: {self.__account_no}\nName: {self.__name}\nBalance: {self.__balance}")


class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_acc(self):
        acc_no = int(input("\nEnter Account Number: "))

        if acc_no in self.__accounts:
            print("Account already exists")
        else:
            name = input("Enter account holder's name: ")
            balance = float(input("Enter initial deposit: "))

            if balance < 1000:
                print("Initial deposit should be above 1000")
                return
            
            self.__accounts[acc_no] = BankAccount(acc_no,name,balance)
            print("Account created successfully!")

    def get_account(self,acc_no):
         return self.__accounts.get(acc_no)

    def deposit_money(self):
        acc_no = int(input("\nEnter Account number: "))
        account = self.__accounts.get(acc_no)

        if account:
            amount = float(input("Enter Amount to Deposit: "))
            account.deposit(amount)
        else:
            print("Account not found!")

    def withdraw_money(self):
        acc_no = int(input("\nEnter Account number: "))
        account = self.__accounts.get(acc_no)

        if account:
            amount = float(input("Enter Amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found!")

    def check_balance(self):
        acc_no = int(input("\nEnter Account number: "))
        account = self.__accounts.get(acc_no)

        if account:
            print(f"Available Balance: {account.get_balance()}")
        else:
            print("Account not found!")

    def view_accounts(self):
        if not self.__accounts:
            print("No accounts found!")
        else:
            print("\n---------- Accounts ----------")
            for acc in self.__accounts.values():
                acc.details()
            print("\n------------------------------")

bank = Bank()

while True:
    print("\n---------- Welcome To Our Bank ----------")
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View All Accounts")
    print("5. Check Balance")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        bank.create_acc()
    elif choice == 2:
        bank.deposit_money()
    elif choice == 3:
        bank.withdraw_money()
    elif choice == 4:
        bank.view_accounts()
    elif choice == 5:
        bank.check_balance()
    elif choice == 6:
        print("\nThank You!\n")
        break
    else:
        print("Invalid choice, Try again!")
