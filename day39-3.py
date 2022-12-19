def rev(string):
    s=""
    if len(string)>0:
        s=string[len(string)-1]+rev(string[0:len(string)-1])
    return s
p=input()
print(rev(p))