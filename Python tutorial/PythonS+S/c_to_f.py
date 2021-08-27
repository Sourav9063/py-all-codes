def c_to_f(celsius):
    return 9*celsius/5+32

def f_to_c(faren):
    return (faren-32)/9*5


f=c_to_f(26)


print(c_to_f(00))
print(c_to_f(100))

print(f"{f_to_c(0): .2f}")
