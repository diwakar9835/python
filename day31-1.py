def Oct(num):
    s=oct(num)
    return s[:1]+s[2:]
n=int(input())
print(Oct(n))