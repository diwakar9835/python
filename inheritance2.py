class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class Employee(Person):
  def __init__(self, name, age):
    Person.__init__(self, name, age)

a=Employee("Anura",20)
a.display()