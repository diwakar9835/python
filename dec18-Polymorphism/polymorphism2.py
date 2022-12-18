# Polymorphism with a function $ object
class India():
  def capital(self):
    print("New Delhi is the capital of India")
  def language(self):
    print("Many languages are spoken in India ")
class USA():
  def capital(self):
    print("washington DC id the capital of USA")
  def language(self):
    print("English is the primary language spoken")

def test(obj):
  obj.capital()
  obj.language()
  
obj1=India()
obj2=USA()

test(obj1)
test(obj2)