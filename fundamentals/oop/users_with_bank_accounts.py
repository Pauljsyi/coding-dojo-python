import bank_account
import ctypes

bankacc = bank_account.BankAccount




class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    
    self.joint = bankacc(int_rate = 0.02, balance = 0)
    self.business = bankacc(int_rate = 0.02, balance = 0)
    self.savings = bankacc(int_rate = 0.02, balance = 0)
    
    # jointAcc = self.joint
    # businessAcc = self.business
    # savingsAcc = self.savings

    # accounts = [jointAcc, businessAcc, savingsAcc]

    # print(type(accounts[2]) != 'class')

    
    # print(self.account.display_account_info(account))

    
    # print(f"print account for {name}",self.account.balance)

    
    
    # default attributes
    self.is_rewards_member = False
    self.gold_card_points = 0
  def make_deposit(self,amount, account):
    if (account == 'joint'):
      self.joint.deposit(amount)
    elif (account == 'business'):
      self.business.deposit(amount)
    elif (account == 'savings'):
      self.savings.deposit(amount)
    return self
    
  def make_withdrawal(self, amount, account):
    if (account == 'joint'):
      self.joint.withdraw(amount)
    elif (account == 'business'):
      self.business.withdraw(amount)
    elif (account == 'savings'):
      self.savings.withdraw(amount)
    return self
  # def transfer_money(self, amount, other_user):

  def display_user_balance(self, account):
    # self.account.display_account_info(account)
    if (account == 'joint'):
      self.joint.display_account_info(account)
    elif (account == 'business'):
      self.business.display_account_info(account)
    elif (account == 'savings'):
      self.savings.display_account_info(account)
    return self
    ### why does this print the bank account object location?
    # print("display acc info:", self.account.display_account_info())
    return self
  def display_info(self):
    print(self.name)
    print(self.name)
    print(self.email)
    return self
  def enroll(self):
    if self.is_rewards_member == False:
      self.is_rewards_member = True
      self.gold_card_points += 200
    else:
      print(f"{self.name} is already a member")
    return self
  def spend_points(self, amount):
    if (self.is_rewards_member and amount <= self.gold_card_points):
      self.gold_card_points -= amount
    else:
      print('not enough points')
    return self



  
  # .make_deposit(50).display_user_balance("joint")
george = User("George Lucas", "starwars123@gmail.com")
# george = User("George Lucas", "starwars123@gmail.com", "savings").make_deposit(500000).display_user_balance("savings")

# define accounts for make_deposit, make_withdrawal, display_user_balance

george.make_deposit(500, 'joint').display_user_balance('joint').make_withdrawal(50, 'joint').display_user_balance('joint')

george.make_deposit(50_000, 'business').display_user_balance('business').make_withdrawal(23_000, 'business').display_user_balance('business')

george.make_deposit(100_000, 'savings').display_user_balance('savings').make_withdrawal(53_000, 'savings').display_user_balance('savings')


"""
SAME INSTANCE?
# george.make_deposit(500, "joint").display_user_balance()
# george.make_deposit(1000, "business").display_user_balance()
# # george.make_deposit(5_000_000, "savings").display_user_balance()
# george.make_deposit(5_000_000, "savings").display_user_balance()

"""

# george.deposit(101).display_account_info()
# george.savings.deposit(101).display_account_info().withdraw(500).display_account_info()
# george.savings.deposit(5_000).display_account_info()
# george.business.deposit(100_000_000).display_account_info().withdraw(500000)

# george.business.display_account_info()
# # george.display_user_balance()
# pablo = User("Pablo Escobar", "kingpin@gmail.com").enroll().spend_points(50).display_info()
# adrian = User("Adrian","Brody", "brodyquest@gmail.com", "45")

# # print(george.display_info())
# # print(george.is_rewards_member)
# # print(george.gold_card_points)
# # print(george.enroll())
# # print(george.is_rewards_member)
# # print(george.gold_card_points)

# adrian.enroll()
# adrian.spend_points(13)
# print(adrian.gold_card_points)

# george.enroll()
# print("points after enroll: ",george.gold_card_points)
# george.spend_points(50)
# print("points after spending x points: ", george.gold_card_points)

# pablo.enroll()
# pablo.spend_points(80)

# # will print "not enough points"
# pablo.spend_points(200)

# # george.display_info()
# # pablo.display_info()
# # adrian.display_info()


# george.enroll()