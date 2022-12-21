def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=int(input("n: "))
x=int(input("x: "))
s=1
for i in range(1,n+1):
    s+=(x**3)/factorial(i)
print("%.2f"%s)