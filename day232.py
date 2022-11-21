import math 
a=int(input())
if a <=180:
    print(round(math.radians(a)))
else:
    print("Enter valid angle")