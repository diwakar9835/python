def remove(str1,ind):
    if(ind<len(str1)):
        print(str1[0:ind+1]+str1[ind+2:])
    else:
        print("Index out of range")
    remove(input(),int(input()))