try:
    print(a)
except NameError:
    print("a is not defined")
except:
    print("Something is not working")