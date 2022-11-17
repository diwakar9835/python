#prime number
num=int(input("Enter the number"))
if num>1:
  for i in range(2,num):
    print(num, "is not a prime number")
    break
else:
  print(num, "is a prime number")
