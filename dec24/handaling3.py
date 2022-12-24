f = open("vy.txt","r")
f.write("Hi I am append")
f.close()

f = open("vy.txt","r")
print(f.read())