pr=int(input("Enter the percentage"))
if pr<40:
    print("Your Category is: Failed")
elif pr>=40 and pr<55:
    print("Your Category is: Fair")
elif pr>=55 and pr<65:
    print("Your Category is: Good")
elif pr>=65 and pr<=100:
    print("Your Ctegory is: Excellent")
elif pr>100:
    print("Please enter correct percentage")