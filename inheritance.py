#inheritance
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class Employee(Person):
  pass
a = Employee("Anurag",20)
a.display()