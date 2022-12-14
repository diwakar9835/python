a=input()
a=a.split(" ")
b=[int(i) for i in a]
c=set(b)
d=max(c)
c.remove(d)
print(max(c))