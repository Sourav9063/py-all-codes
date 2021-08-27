import string

print("Pangram") if len(set(input("Enter sth:").lower().replace(' ', ''))) >= 26 else print("Not pangram")

# print(set(my_input))


#
# for letter in string.ascii_lowercase:
#     # print(letter in my_input == False)
#     if letter not in my_input:
#         print("Not pangram")
#         break
#         # print(letter)
# else:
#     print("Pangram")
