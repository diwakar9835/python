age=int(input("Enter your age"))

sex=input("Enter sex(M/F)") 
nd= int(input("Enter number of days"))
if age>=18 and age < 30 and sex.upper() == 'M':
    amt = nd*700
    print("Total wages is : ", amt) 
elif age >=18 and age < 30 and sex.upper() == "F":
    amt = nd*750
    print("Total wages is: ", amt)
elif age >30 and age <= 40 and sex.upper() == 'M':
    amt = nd* 800
    print("Total wages is: ", amt)
elif age >=30 and age <= 40 and sex.upper() == 'F': 
    amt = nd* 850
    print("Total wages is: ", amt)
else: print("Enter appropriate age")