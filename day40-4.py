a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)
print([int(j) for j in b])
print(tuple([int(j) for j in b]))