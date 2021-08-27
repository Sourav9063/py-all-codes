thisIsAList = [1, 2, 3, 4]
thisIsAList[0] = -0
print(thisIsAList)

thisIsATuples = (1, 2, 3, 4)
# thisIsATuples.append(5)
listToTuples = tuple(thisIsAList)

print(type(listToTuples))

tupleToList = list(thisIsATuples)

print(type(tupleToList))

thisISADict = {'name': "Sourav", 'lover': "Sayma", 'since': 2019, 'List': [1, 2, 3, 4, 5, 6, 7], 'LoverName': "Sayma"}
#
print(thisISADict['lover'])
#
thisISADict['last name'] = "Ahmed"
#
print(thisISADict)

myList = [2, 2, 2, 1, 1, 1, 3, 3, -1, 3, 9]

uniqueList = set(myList)
for i in myList:
    if not (i in uniqueList):
        uniqueList.append(i)
print(uniqueList)
name = "Sourav Ahmed"
listOfLetters = []
for letter in name:
    listOfLetters.append(letter)
print(listOfLetters)

myList = ['Sourav', 'Ahmed', ['Sayma', ['Sharmin'], 'Rahmam']]

myList[2].append("Pramanik")
myList[2].insert()

print(myList)
