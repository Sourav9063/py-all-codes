myFile = open("1stfile.txt", "w")

myFile.write("Sayma ")
myFile.write("Ahmed\n")
myFile.writelines(["Sayma Sultana\n", "Loves me\n"])
myFile.writelines("She is a good girl\n")

myFile.close()

with open("1stfile.txt", 'r') as myFile:
    print(myFile.readlines())
    myFile.seek(0)
    print(myFile.readlines())
print("End")

