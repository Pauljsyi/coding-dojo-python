class BankAccount:
  def __init__(self, int_rate = 0.01, balance = 0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount
    # print(self.balance)
    return self
    
  def withdraw(self, amount):
    if (self.balance >= amount):
      self.balance -= amount
    else:
      self.balance -= 5
      print('insufficient funds: Charging a $5 fee')
    return self

  def display_account_info(self):
    print(f"You have ${self.balance} in your account")
    return self

  def yield_interest(self):
    if (self.balance > 0):
      yielded_int = self.balance * (1 + self.int_rate)
      print(yielded_int)
    return self
  @classmethod
  

user1 = BankAccount()
user2 = BankAccount()

user1.display_account_info().deposit(50).display_account_info().withdraw(50).display_account_info()

