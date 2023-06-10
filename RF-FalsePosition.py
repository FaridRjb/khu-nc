def false_pos(f, a, b, acc, steps=False):
    
    count = 0

    if f(a) == f(b):
        return None, count

    while True:
        count += 1
        x0 = - f(a)*(b - a)/(f(b) - f(a)) + a
        if steps: print(a, b, x0, count)
        if abs(f(x0)) < acc:
            break
        if f(a) * f(x0) > 0:
            a = x0
        else:
            b = x0
    return x0, count


def f(x):
    return x**2 - 5

print(false_pos(f, -4, 4, 0.01, True))
