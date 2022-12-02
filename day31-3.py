def productof(n):
    if n<10:
        return n%10
    return (n%10)*productof(int(n//10))
print(productof(int(input())))