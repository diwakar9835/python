def perfect_fourth(a,b) :
    for i in range(a,b):
        if round(i**(1/4))**4==i:
            return i
a=int(input())
b=int(input())
print(perfect_fourth(a,b))