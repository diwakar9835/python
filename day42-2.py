def is_leap(year):
    if year%4==0 and year%100!=0:
        print("31622400")
    elif year%100==0:
        print("-1")
    elif year%400==0:
        print("31622400")
    else:
        print("-1")
is_leap(int(input()))