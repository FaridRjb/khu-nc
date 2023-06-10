def newton(f, x0, acc, steps=False):
    
    count = 0

    if abs(f(x0)) < acc:
        return x0, count

    while True:
        count += 1
        df = (f(x0 + acc/2) - f(x0 - acc/2)) / acc
        x0 = x0 - f(x0)/df
        if steps: print(x0, count)
        if abs(f(x0)) < acc:
            break
    return x0, count


def f(x):
    return x**2 + 3 * x - x**3

print(newton(f, 1.5, 0.01, True))
