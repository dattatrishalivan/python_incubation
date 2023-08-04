"""Create a class BankAccount, which contains attributes balance and name, and methods
deposit() and withdraw(), to add and deposit some money in account.
the balance should be set to 0 in the constructor, and withdrawal should be allowed only if
sufficient balance is there. Also overload the str method to allow printing the details directly."""


class BankAccount:
    balance = 0
    name = 'dattatri'

    def __init__(self):
        self.balance = 0

    def deposit(self, dep):
        self.balance = self.balance + dep

    def withdrwal(self, withd):
        if self.balance >= withd:
            self.balance = self.balance - withd
            self.__str__()
        else:
            print("insufficient balance please renter")

    def __str__(self):
        print(f'Thank you {self.name} for using service  your remaiming balance is {self.balance}')


b = BankAccount()
dep = int(input("enter amount to deposit : "))
wit = int(input("enter amount to withdrawl : "))
b.deposit(dep)
b.withdrwal(wit)
