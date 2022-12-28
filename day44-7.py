s=input()
l=""
u=""
for i in s:
    if i.isupper():
        u+=i
    else:
        l+=i
print(u+l)

