def fact(n):
    if(n==1 or n==0):
        return n
    else:
        return n*(fact(n-1))
def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))
n=int(input("Enter n: "))
r=int(input("Enter r: "))
print(int(combination(n,r)))