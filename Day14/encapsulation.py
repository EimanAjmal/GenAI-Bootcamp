class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount()

account.show_balance()