#Reverse a number
numb = int(input("Enter the number to be reversed"))#1234
rev = 0
while (numb > 0):
  #logic
  remainder = numb % 10 #4
  rev = (rev * 10) + remainder #rev = 4
  numb = numb // 10 #123
  #print(rev)
print("The reverse of the number is: {}".format(rev)) 
