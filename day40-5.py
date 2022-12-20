s=""
def Base7(num):
    global s
    s=str(num%7)+s
    if(num//7!=0):
        Base7(num//7)
    else:
        s="0"+s
        return s
print(Base7(int(input())))