def digit(*args):
    s=""
    for i in args:
        s=s+i
    print(s)
a=input()
b=input()
c=input()
d=input()
e=input()
l=[a,b,c,d,e]
digit(*l)