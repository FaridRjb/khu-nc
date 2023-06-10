def bisec(f, a, b, acc, steps=False):
    
    count = 0

    if f(a) * f(b) > 0:
        return None, count

    while True:
        count += 1
        x0 = (a + b)/2
        if steps: print(a, b, x0, count)
        if abs(f(x0)) < acc:
            break
        if f(a) * f(x0) > 0:
            a = x0
        else:
            b = x0
    return x0, count


def f(x):
    return x**2 - 3 * x + x**3

print(bisec(f, -2, 0, 0.1, True))
