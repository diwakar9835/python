class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class Employee(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.year=year
  def welcome(self):
    print("Welcome",self.name,"you are",self.age,"years old","your year is",self.year)
a=Employee("Anurag",20,2022)
a.welcome()