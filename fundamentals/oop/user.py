class User:
  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    # default attributes
    self.is_rewards_member = False
    self.gold_card_points = 0
  def display_info(self):
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print(self.age)
  def enroll(self):
    if self.is_rewards_member == False:
      self.is_rewards_member = True
      self.gold_card_points += 200
    else:
      print(f"{self.first_name} is already a member")
  def spend_points(self, amount):
    if (self.is_rewards_member and amount <= self.gold_card_points):
      self.gold_card_points -= amount
    else:
      print('not enough points')


george = User("George", "Lucas", "starwars123@gmail.com", "12")
pablo = User("Pablo", "Escobar", "kingpin@gmail.com", "4")
adrian = User("Adrian","Brody", "brodyquest@gmail.com", "45")

# print(george.display_info())
# print(george.is_rewards_member)
# print(george.gold_card_points)
# print(george.enroll())
# print(george.is_rewards_member)
# print(george.gold_card_points)

adrian.enroll()
adrian.spend_points(13)
print(adrian.gold_card_points)

george.enroll()
print("points after enroll: ",george.gold_card_points)
george.spend_points(50)
print("points after spending x points: ", george.gold_card_points)

pablo.enroll()
pablo.spend_points(80)

# will print "not enough points"
pablo.spend_points(200)

# george.display_info()
# pablo.display_info()
# adrian.display_info()


george.enroll()