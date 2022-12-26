# LPU test solution
import math
a=float(input())
if a<-1 or a>1:
    print("invalid")
else:
    print("{:.4f}".format(math.atan(a)))