class user:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0

  def make_deposit(self, amount):
    self.account_balance += amount
    return self
  
  def make_withdrawal(self, amount):
    self.account_balance -= amount
    return self

  def display_user_balance(self):
    print("User: "+self.name+", Balance: $"+str(self.account_balance)) 
    return self

  def transfer_money(self, user, balance):
    self.make_withdrawal(balance)
    user.make_deposit(balance)
    return self



hira = user("Hira Shin", "yadaAthotmail")
aera = user("Aera Shin", "yamaAthotmail")
josh = user("Josh Shin", "yabaAthotmail")

# hira.make_deposit(100)
# hira.make_deposit(50)
# hira.make_deposit(50)
# hira.display_user_balance()
hira.make_deposit(100).make_deposit(50).make_deposit(50).display_user_balance()

# aera.make_deposit(500)
# aera.make_deposit(500)
# aera.make_withdrawal(300)
# aera.make_withdrawal(300)
# aera.display_user_balance()
aera.make_deposit(500).make_deposit(500).make_withdrawal(300).make_withdrawal(300).display_user_balance()

# josh.make_deposit(200)
# josh.make_withdrawal(100)
# josh.make_withdrawal(100)
# josh.make_withdrawal(100)
# josh.display_user_balance()
josh.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# hira.transfer_money(aera, 100)
# hira.display_user_balance()
# aera.display_user_balance()
hira.transfer_money(aera, 100).display_user_balance()
aera.display_user_balance()