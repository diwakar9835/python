def second_half(str1):
    l=len(str1)
    if l%2==0:
        l=l//2
        return str1[l:]
    else:
        l=l+1
        l=l//2
        return str1[l-1:]
n=input()
print(second_half(n))