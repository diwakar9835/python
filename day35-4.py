a=input()
s=""
for i in a:
    if(i not in s):
        s+=i
for i in s:
    print(i+"@",end="")
print()