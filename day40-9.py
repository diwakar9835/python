pi = 3.142
radius = 5
def circle(n):
    global radius
    radius = radius * n
    area_of_circle=pi*(radius)**2
    print("{:.2f}".format(area_of_circle))
n=int(input())
circle(n)