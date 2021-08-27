import math


def count_primes(num):
    primes = [2]
    strt = 3
    if num < 2:
        return 0
    while strt <= num:
        for x in range(3, int(math.sqrt(strt)), 2):
            if strt % x == 0:
                strt += 2
                break
        else:
            # primes.append(strt)
            print(strt)
            strt += 2
    print(primes)
    return len(primes)


count_primes(100)


# myList = [1, "Two", 3, 5, 6, 7]
#
# for num in myList:
#     if num==5:
#         break
# else:
#     print("The loop didn't break")

# num = int(input("Enter num: "))
#
# for i in range(2, num//2):
#     if num % i == 0:
#         print("Not prime. Divisible by", i)
#         break
# else:
#     print("Prime")
