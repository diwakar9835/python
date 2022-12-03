import math
n = int(input())
for i in range(1,n+1):
    s=sum([math.factorial(int(j)) for j in str(i)])
    if s==i:
        print(i+1,end=' ')