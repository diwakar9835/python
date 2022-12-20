def cube(n):
    return n**3
def triple(n):
    return n*3
n=int(input())
print(triple(cube(n)))
print(cube(triple(n)))