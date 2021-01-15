class BankAccount:
  def __init__(self, int_rate, balance=0):
    self.balance = balance
    self.int_rate = int_rate
    self.checkings = balance
    self.savings = 0

  def deposit(self, amount, type):
    self.balance += amount
    if type == "checkings":
      self.checkings += amount
    if type == "savings":
      self.savings += amount
    return self

  def withdraw(self, amount, type):
    self.balance -= amount
    if type == "checkings":
      self.checkings -= amount
    if type == "savings":
      self.savings -= amount
    if self.balance < 0:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
    return self

  def display_account_info(self):
    print("Balance: $", self.balance)
    print("Checking Balance: $", self.checkings)
    print("Savings Balance: $", self.savings)
    return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance*self.int_rate
    return self

# acct1 = BankAccount(.01, 100)
# acct2 = BankAccount(.01, 500)

# acct1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()

# acct2.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()