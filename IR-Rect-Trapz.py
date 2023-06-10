from math import sin, cos

def rect_trap(f, a, b, n):

    res_l, res_m, res_r, res_t = 0, 0, 0, 0
    h = (b - a)/n
    
    for i in range(0, n):
        xn = a + i * h
        res_l += h * f(xn)
        res_m += h * f(xn + h/2)
        res_r += h * f(xn + h)
        res_t += h * (f(xn) + f(xn + h)) / 2
    return res_l, res_m, res_r, res_t


def f(x):
    return sin(cos(2 * x)) / x

print(rect_trap(f, 2, 6, 10))
