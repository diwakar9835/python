def check(a,b):
    for i in b:
        if i not in a:
            return False
    return True
a=input()
b=input()
print(check(a,b))