def geometric_sum(n):
    sum1=0
    for i in range(1,n):
        sum1=sum1+(1/i**2)
    return "{:.6f}".format(sum1)
print(geometric_sum(int(input())))