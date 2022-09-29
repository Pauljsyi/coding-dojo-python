from collections import UserList
import bank_account
import ctypes

BankAccount = bank_account.BankAccount




class User:
  def __init__(self, name, email, int_rate, balance, acct_type):
    self.name = name
    self.email = email
    self.acct_type = acct_type
    self.account = BankAccount(int_rate, balance, acct_type)
    print("current account type: ", self.acct_type)
    # default attributes
    self.is_rewards_member = False
    self.gold_card_points = 0
  def make_deposit(self,amount, acct_type):
    all_acct = self.account.all_accounts
    # print(all_acct[2].acct_type)
    # print(self.acct_type)
    for i in range(len(all_acct)):
      print(all_acct[i].acct_type)
      if all_acct[i].acct_type == acct_type:
        self.account.deposit(amount)
        print(f'successfully deposited ${amount} to your {self.acct_type} account')
    return self
  def make_withdrawal(self, amount):
    self.account.withdraw(amount)
    return self
  def display_user_balance(self):
    self.account.display_account_info(self.acct_type)
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



  # def __init__(self, name, email, int_rate, balance, acct_type):
# george = User("George Lucas", "starwars123@gmail.com", 0.02, 5, "savings").make_deposit(50).display_user_balance()
# george = User("George Lucas", "starwars123@gmail.com", None, 5, "checkings").make_deposit(100).display_user_balance()
# george = User("George Lucas", "starwars123@gmail.com", 0.4, 5, "business").make_deposit(41000).display_user_balance().make_withdrawal(500).display_user_balance()
george = User("George Lucas", "starwars123@gmail.com", 0.02, 5, "savings")
george = User("George Lucas", "starwars123@gmail.com", None, 5, "checkings")

george = User("George Lucas", "starwars123@gmail.com", 0.4, 5, "business")
george.make_deposit(50,"savings").display_user_balance()

# george = [User("George Lucas", "starwars123@gmail.com", 0.02, 5, "savings"),
# User("George Lucas", "starwars123@gmail.com", None, 5, "checkings"),
# User("George Lucas", "starwars123@gmail.com", None, 5, "business")]
# print(george.account.all_accounts[0].acct_type)
# print(george.account.all_accounts[1].acct_type)
# print(george.account.all_accounts[2].acct_type)

# george.account.all_accounts[0].acct_type[0] = "loans"

# print(george.account.all_accounts[0].acct_type[0])
# define accounts for make_deposit, make_withdrawal, display_user_balance

# george.make_deposit(500).display_user_balance().make_withdrawal(50, ).display_user_balance()

# george.make_deposit(50_000).display_user_balance().make_withdrawal(23_000).display_user_balance()

# george.make_deposit(100_000).display_user_balance().make_withdrawal(53_000).display_user_balance()

# george.make_deposit(50).account.all_accounts

# print(george.account.all_accounts)
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