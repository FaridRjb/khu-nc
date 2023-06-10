
# f1 = p' : K
# f2 = y' : L

def p_prime(x, y, p):
    return 64 * y - 10

def y_prime(x, y, p):
    return p

x0 = 0
y0 = 1
y_prime0 = 1
# p = y'
p0 = y_prime0

x = 0.2
n = 1e4
h = (x - x0) / n

xn = x0
yn = y0
pn = p0




while xn < x:
    K1 = h * p_prime(xn, yn, pn)
    L1 = h * y_prime(xn, yn, pn)
    K2 = h * p_prime(xn + h/2, yn + K1/2, pn + L1/2)
    L2 = h * y_prime(xn + h/2, yn + K1/2, pn + L1/2)
    K3 = h * p_prime(xn + h/2, yn + K2/2, pn + L2/2)
    L3 = h * y_prime(xn + h/2, yn + K2/2, pn + L2/2)
    K4 = h * p_prime(xn + h, yn + K3, pn + L3)
    L4 = h * y_prime(xn + h, yn + K3, pn + L3)

    pn1 = pn + (K1 + 2*K2 + 2*K3 + K4) / 6
    yn1 = yn + (L1 + 2*L2 + 2*L3 + L4) / 6
    
    xn += h
    pn = pn1
    yn = yn1

print(yn)

