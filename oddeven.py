#taking the number from the user and check the number is odd or even
num=int(input("Enter the number to check if it is even or odd ")) # this line will take an input from the user
#if the number s divisible by 2 it is even else it is odd
if num%2 == 0:
    print(num, "is even number")
else:
    print(num, "is an odd number")