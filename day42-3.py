def LCM(a, b):
    t=a%b
    if t==0:
        return a
    return a*LCM(b,t)/t
a=int(input())
b=int(input())
m=LCM(a,b)**3
print(int(m))