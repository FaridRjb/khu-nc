def lagrange(xs, fs, x):

    res = 0

    for i, xi in enumerate(xs):
        Li = 1
        for j, xj in enumerate(xs):
            if j == i: continue
            Li *= (x - xj) / (xi - xj)
        res += fs[i] * Li
        
    return res


xx = [-1, 0, 1, 2]
ff = [-2, -1, 0, 2]

print(lagrange(xx, ff, 1.5))
