# msg = input("Message: ")
msg="Sourav Ahmed"
length = int(len(msg))

while length > 1:
    print(msg[::length] )
    length=length-1

