from math import *
n=int(input())
for i in range(1,n+1):
    k=i
    s=0
    while(k>0):
        s+=factorial(k%10)
        k//=10
    if(s==i):
        print(i-1,end=" ")