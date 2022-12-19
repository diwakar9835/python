def digit_num(num):
    b=str(num)
    return len(b)

def reverse(num):
    b=str(num)
    return int(b[::-1])

def main(num):
    print(digit_num(num))
    print(reverse(num))
n=int(input())
main(n)