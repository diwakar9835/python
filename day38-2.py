def power(base,exp):
    if(exp!=2):
        return base*power(base,exp-1)
    else: return base
print(power(int(input()),int(input())))