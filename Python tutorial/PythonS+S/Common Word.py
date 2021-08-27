def cmmn_letter(name1, name2):
    '''Returns common letter's list'''
    cmmn_letter_list = []
    for letter in name1.upper().replace(" ", ''):
        if letter in name2.upper().replace(" ", ''):
            cmmn_letter_list.append(letter)
    return sorted(set(cmmn_letter_list))


ans = cmmn_letter("Sourav Ahmed", "Sayma Sultana")
ans2 = cmmn_letter("Kaniz nazma", "Sayma Sultana")
print(ans, ans2)
