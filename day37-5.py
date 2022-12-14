n=int(input())
z=[]
for i in range(n):
    y=[int(i) for i in input().split(',')]
    z.append(tuple(y))
z.sort(key=lambda x: sum(x))
print(tuple(z))