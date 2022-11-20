s1=int(input("Enter first side of traingle"))
s2=int(input("Enter second side of traingle"))
s3=int(input("Enter third side of traingle"))
if s1==s2 and s2==s3:
    print("Equilateral traingle")
if (s1==s2 and s2!=s3) or (s2==s3 and s2!=s1) or (s1==s3 and s1!=s2):
    print("Isosceles Traingle")
if s1!=s2 and s1!=s3 and s2!=s3:
    print("Scalene Traingle")