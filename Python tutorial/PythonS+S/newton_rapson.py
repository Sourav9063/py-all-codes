def f(x):
    return x**3 - 2*x**2 + x - 1
def df(x):
    return 3*x**2 - 4*x + 1
def df_function(f,x):
    h = 0.00000001
    return (f(x+h)-f(x))/h
def newton_rapson(f,x, excepted_error, nmax):
    x0 = x
    for i in range(nmax):
        error_percent=100
        x1 = x0 - f(x0)/df(x0)
        if(x1 != 0):
            error_percent = abs((x1 - x0)/x1)*100
        x0 = x1
        print("Iteration:", i, "x:", x1, "Error:", error_percent)
        if error_percent < excepted_error:
            return x1
    print("There is no root")
    return None

ans=newton_rapson(f,10,0.00001,100)
print("The root is:", ans)