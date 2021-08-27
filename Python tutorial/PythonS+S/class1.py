import string
# for i in range(int(input())):
#     a, b = map(int, input().split())
#     print(abs(a - b) // 10 + 1)
print(string.ascii_letters)

s=input("Enter sentence")

if set(string.ascii_lowercase)==set(s.lower().replace(' ','')):
    print("Pangram")
else:
    print("Not pangram")
print(set(string.ascii_lowercase))