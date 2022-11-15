#priting a pattern using nested for loop
n=int(input())
for i in range(0,n):
  for j in range (0,i+1):
    print("*",end="")
  print()