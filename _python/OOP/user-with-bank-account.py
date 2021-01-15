
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

class User:
  def __init__(self, name, email, balance, int_rate=0.02):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate, balance)

  def make_deposit(self, amount, type):
    self.account.deposit(amount, type)
    return self
  
  def make_withdrawal(self, amount, type):
    self.account.withdraw(amount, type)
    return self

  def display_user_balance(self):
    print("User: "+self.name)
    self.account.display_account_info()
    return self

  def transfer_money(self, user, balance):
    self.make_withdrawal(balance)
    user.make_deposit(balance)
    return self



hira = User("Hira Shin", "yadaAthotmail", 500)
aera = User("Aera Shin", "yamaAthotmail", 1000)
josh = User("Josh Shin", "yabaAthotmail", 2000)

hira.display_user_balance()
aera.make_deposit(500, "checkings").display_user_balance()
josh.make_withdrawal(500, "savings").display_user_balance()
