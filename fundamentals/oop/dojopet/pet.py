from sub_pets import Troy
from sub_pets import Cody
from sub_pets import Penny


class Pet():
  def __init__(self, name , type , tricks):
    super().__init__(name)
    self.name = name
    self.type = type
    self.tricks = tricks
    self.energy = 100
    self.health = 100
    print(super().name)

  # implement the following methods:
  # sleep() - increases the pets energy by 25
  def sleep(self):
    self.energy += 25
    print(f'energy level rose by 25 points ... current energy level {self.energy}')
  # eat() - increases the pet's energy by 5 & health by 10
  def eat(self):
    self.energy += 5
    self.health += 10
    print(f'energy level rose by 5 points and health rose by 10 points  ... current energy level {self.energy}  ... current health level {self.health}')
  # play(self) - increases the pet's health by 5
  def play(self):
    self.health -= 5
    print(f'health -5 points  ... current health level {self.health}')
  # noise() - prints out the pet's sound
  def noise(self, sound):
    print(f"Your pet {self.name} let out a {sound}")

#   def __init__(self, name , type , tricks):
    # super().__init__(name)
troy = Troy('troy', 'german shepherd', 'bark')
cody = Cody('cody', 'dachschund', 'run')
penny = Penny('penny', 'dachschund', 'bite')