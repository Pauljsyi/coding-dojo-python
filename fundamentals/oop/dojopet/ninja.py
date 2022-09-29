from sub_pets import Troy
from pet import Pet

class Ninja(Pet):
  def __init__( self, first_name , last_name , treats , pet_food , pet ):
    self.first_name = first_name
    self.last_name = last_name
    self.treats = treats
    self.pet_food = pet_food
    self.pet = pet
    # print(self.first_name)
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
  def walk(self):
    self.pet.play()
    return self
# feed() - feeds the ninja's pet invoking the pet eat() method
  def feed(self):
    self.pet.eat()
    return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
  def bathe(self, sound):
    self.pet.noise(sound)
    return self

# class Ninja:
  # def __init__( self, first_name , last_name , treats , pet_food , pet )
# class Pet:
  # def __init__( self, name , type , tricks )
george = Ninja('george', 'yi', 'turkey', 'kibble', Pet(Troy)).bathe()

