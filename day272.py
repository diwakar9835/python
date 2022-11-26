def my_sum(*args):
    return(sum(args))
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
sdf=[a,b,c,d,e]
print (my_sum(*sdf))