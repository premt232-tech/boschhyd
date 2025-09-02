class Bank:
    def __init__(self, name, accno, bal=500.0):
        self.name = name
        self.accno = accno
        self.bal = bal

    def getBalance(self):
        return self.bal

    def getDeposit(self, dep):
        self.bal += dep
        print("Your money is deposited")

    def withdrawal(self, withdraw):
        if self.bal >= withdraw:
            self.bal -= withdraw
            print("Collect your money")
        else:
            print("Insufficient money")

    def __str__(self):
        return f"Account[{self.accno}] - {self.name}, Balance: ₹{self.bal:.2f}"


class SavingsAccount(Bank):
    def apply_interest(self, interest_rate):
        interest = self.bal * interest_rate
        self.bal += interest
        print(f"Interest of ₹{interest:.2f} applied.")


class CurrentAccount(Bank):
    def __init__(self, name, accno, overdraft_limit, bal=500.0):
        super().__init__(name, accno, bal)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.bal + self.overdraft_limit:
            self.bal -= amount
            print(f"Withdrew ₹{amount:.2f} (Overdraft used if needed)")
        else:
            print("Insufficient money")


def testcase():
    f1 = SavingsAccount("Prem", "001", 100000)
    print(f1.getBalance())
    f1.getDeposit(50000)
    f1.withdrawal(10000)
    print(f1)
    f1.apply_interest(0.05)  # 5% interest
    b2 = CurrentAccount("bharth","001", 10000,1000000)
    b2.withdraw(5000)
    print(b2)
testcase()
