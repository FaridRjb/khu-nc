
def rk2(f, h, bc, x):

    x0, y0 = bc
    
    xn = x0
    yn = y0
    yn_2 = [yn]
    while xn < x:
        K1 = h * f(xn, yn)
        K2 = h * f(xn + h, yn + K1)
        yn1 = yn + (K1 + K2) / 2
        xn += h
        yn = yn1
        yn_2.append(yn)
    sol = yn
    
    return sol, yn_2

def rk4(f, h, bc, x):

    x0, y0 = bc

    xn = x0
    yn = y0
    yn_4 = [yn]
    while xn < x:
        K1 = h * f(xn, yn)
        K2 = h * f(xn + h/2, yn + K1/2)
        K3 = h * f(xn + h/2, yn + K2/2)
        K4 = h * f(xn + h, yn + K3)
        yn1 = yn + (K1 + 2*K2 + 2*K3 + K4) / 6
        xn += h
        yn = yn1
        yn_4.append(yn)
    sol = yn

    return sol, yn_4


def f(x, y):
    return 1 - y**2

sol, _ = rk4(f, 0.1, (0, 0), 0.1)
print(sol)
