a=int(input())
b=0
for x in range (4):
    b=b+(a%10)
    a=a//10
print(b)