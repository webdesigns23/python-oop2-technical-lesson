class Dog:
  def __init__(self, name, breed, age, last_checkup = None):
    self.name = name
    self.breed = breed
    self.age = age
    self.last_checkup = last_checkup

  def get_age(self):
    return self._age
  def set_age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      print("Not valid age")
  age = property(get_age,set_age)