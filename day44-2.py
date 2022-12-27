s=input()
k=""
for i in s:
    if(i not in k):
        k+=i
for i in k:
    print(i,":",s.count(i))