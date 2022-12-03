def length(str1):
    return len(str1)
s="abcdstu"
i=input()
print(len(i))
l=''
for x in i:
    if x not in s:
        l += x
print(len(l))