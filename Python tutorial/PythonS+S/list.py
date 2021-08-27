def letter_from_word(word):
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    return letter_list


mainFuncWord = input("Input : ")

lst_of_letter = letter_from_word(mainFuncWord)
print(lst_of_letter)
