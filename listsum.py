# write the program to claculate the sum of numbers in the list
sum = 0
i = 0

list1 = [2,3,4,1]

while i < len(list1):
  sum = sum + list1[i]
  i=i+1
  print("The sum of all the numbers in the list is",sum)