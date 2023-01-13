def f(x):
    y = x ** 2 - 5 * x - 2
    return y


def regular_falsi(f, a, b, epsilon):
    if f(a) * f(b) < 0:

        for i in range(1000):
            x0 = (a * f(b) - b * f(a)) / (f(b) - f(a))

            if abs(f(x0)) <= epsilon:
                return x0
            else:
                if f(a) * f(x0) < 0:
                    b = x0
                else:
                    a = x0
    elif f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    else:
        return "No root"


a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))
epsilon = float(input("Enter epsilon: "))

ans = regular_falsi(f, a, b, epsilon)
print("Root is: ", ans)
