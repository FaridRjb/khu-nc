def newton(xs, fs, steps=False):

    res = [fs]

    while len(res[-1]) > 1:
        f = res[-1]
        new_f = []
        for i in range(0, len(f)-1):
            x_step = len(res)
            item = (f[i] - f[i+1]) / (xs[i] - xs[i + x_step])
            new_f.append(item)
        res.append(new_f)
        
    return res


xx = [0, 1, 2, 4]
ff = [1, 1, 2, 5]

print(newton(xx, ff, True))
