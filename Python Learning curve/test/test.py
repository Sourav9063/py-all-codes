x=100
def change_x():
    global x
    x=30
    return x

print(x)
change_x()
print(change_x())
print(x)