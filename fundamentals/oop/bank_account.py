class BankAccount:
  all_accounts = []
  

  def __init__(self, int_rate, balance, acct_type):
    self.acct_type = acct_type
    self.int_rate = int_rate
    self.balance = balance
    BankAccount.all_accounts.append(self)
    
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

  def display_account_info(self, acct):
    print(f"You have ${self.balance} in your {acct} account")
    return self
  def display_acct_info(self, acct):
    print(f"You have ${self.balance} in your {acct} account")
    return self
  def yield_interest(self):
    if (self.balance > 0):
      yielded_int = self.balance * (1 + self.int_rate)
      print(yielded_int)
    return self
  @classmethod
  def print_all(cls):
    for account in cls.all_accounts:
      print(account)

# account1 = BankAccount().deposit(50).display_acct_info()
# account2 = BankAccount().deposit(31)
# user3 = BankAccount().deposit(600).display_acct_info().print_all()

# account1 = BankAccount()
# account2 = BankAccount()
# user3 = BankAccount()

# BankAccount().print_all()

# print(BankAccount().all_accounts)

# user1.display_account_info().deposit(50).display_account_info().withdraw(50).display_account_info()


# the instance with $0 
# BankAccount().print_all()

