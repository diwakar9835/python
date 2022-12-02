def geometric_sum(n):
    sum=0
    for i in range(1,n):
        c=1/(i)**2
        sum+=c
    return sum
n=int(input())
print(format(geometric_sum(n),".6f"))