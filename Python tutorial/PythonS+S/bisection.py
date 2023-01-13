degree=int(input("Enter the degree of the polynomial: "))
coeff=[0]*(degree+1)
for i in range(degree+1):
    coeff[i]=float(input(f"Enter the coefficient of x^{i}: "))


def f_poly(x):
    y=0
    for i in range(degree+1):
        y+=coeff[i]*(x**i)
    return y


def bisection(f,a,b,epsilon):
    if f(a)==0:
        return a
    elif f(b)==0:
        return b
    elif f(a)*f(b)<0:
        mid=(a+b)/2
        while abs(a-b)>=epsilon:

            if f(mid)==0:
                return mid
            elif f(a)*f(mid)<0:
                b=mid
            else:
                a=mid
            mid=(a+b)/2
        return mid
    else:
        print("No root exists")


a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
epsilon=float(input("Enter the precision: "))
ans=bisection(f_poly,a,b,epsilon)
print(ans)


