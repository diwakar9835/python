
print ("Number of classes held")
noh = float(input())
print ("Number of classes attended")
noa = float(input())
atten = (noa/float(noh))*100
print ("Attendence is",atten)
if atten >= 75:
  print ("You are allowed to sit in exam")
else:
  print ("Sorry, you are not allowed. Attend more classes from next time.")