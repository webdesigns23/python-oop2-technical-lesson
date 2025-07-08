class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.vets = []
    self.checkups = []

  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      raise ValueError("Not valid age")
    
  def add_checkup(self, vet, date, notes):
    if vet not in self.vets:
      self.vets.append(vet)
    new_checkup = {
      "vet": vet,
      "date": date,
      "notes": notes
    }
    self.checkups.append(new_checkup)

  def find_checkup(self, date):
    for checkup in self.checkups:
      if checkup["date"] == date:
        print(f"Checkup on {date} by {checkup["vet"]}: {checkup["notes"]}")
        return print(f"No checkup found on {date}")
        
fido = Dog(
   name = "Fido",
   age = 3, 
   breed = "Golden Retriever"
   )
fido.add_checkup("Doolittle", "02/20/22","Good health!")
print(fido.vets)
print(fido.checkups)
fido.find_checkup("02/20/22")
fido.find_checkup("03/22/24")        
  