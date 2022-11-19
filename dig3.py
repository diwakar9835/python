num1 = input("Enter any number")

I= len(num1) 
if I != 3:
    print("Enter three digit number")
else:
    print("Middle digit is ",(int(num1)%100//10))
