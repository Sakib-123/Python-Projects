class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"Account '{self.name}' created.\nBalance = ${self.balance:.2f}")


    def getBalance(self):
        print(f"Account '{self.name}' and Balance is '{self.balance:.2f}' ")

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"${self.amount} deposited Successfully.")
        self.getBalance()
        # print(f"Account '{self.name}' and Balance is '{self.balance:.2f}' ")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Account '{self.name}' has only a balance of ${self.balance:.2f}.")

    def withdrawl(self, amount):
        self.amount = amount
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"${self.amount} withdrew Successfully.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdrawl Interrupted: {error}")

    def transfer(self, amount, account):
        self.amount = amount
        try:
            print("Beginning Transfer...")
            self.viableTransaction(amount)
            self.withdrawl(amount)
            account.deposit(amount)
            print("Transfer Completed.")
        except BalanceException as error:
            print(f"Transfer Interrupted &{error}")

class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance += (1.05 * amount)
        self.getBalance()

class SavingsAcc(InterestRewardAcc):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5

    def withdrawl(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw Completed.")
            self.getBalance()

        except BalanceException as error:
            print(f"Withdraw Completed {error}.")



