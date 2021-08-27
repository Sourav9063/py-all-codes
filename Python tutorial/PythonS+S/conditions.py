x = int(input("enter a number"))
if x >= 0:
    print("Positive number")
    print("Another line")
    if x % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")
