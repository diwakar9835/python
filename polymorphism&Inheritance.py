# polymorphism with Inheritance
class Bird:
  def intro(self):
    print("Hi this is bird class")
  def flight(self):
    print("Most of the birds can fly")

class Parrot(Bird):
  def flight(self):
    print("Parrots can fly")

class Ostrich(Bird):
  def flight(self):
    print("Ostrich cannot fly")

obj1 = Bird()
obj2 = Parrot()
obj3 = Ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()