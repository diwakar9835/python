class Student:
  def __init__(self, name, reg):
    self.name=name
    self.reg=reg
  def pr(self):
    print("Hello my name is "+self.name)
s1 = Student("Anurag",12218436)
s1.pr()