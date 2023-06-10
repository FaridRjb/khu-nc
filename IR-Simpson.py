#!/usr/bin/env python
# coding: utf-8

from math import sqrt


def simps_int(f, a, b, h):
    '''
    Integration using the Simpson method.
    
    Params
    ---
    f - function f(x)
    a - int, float : Left limit
    b - int, float : Right limit
    h - int, float : Integration interval that should be (b - a) / n, where n is an even integer.
    
    Returns
    ---
    Integral value.
    '''
    n = int((b - a) / h)
    xs = [a + i*h for i in range(0, n+1)]
    res = 0
    for i in range(0, n, 2):
        res += (h/3) * (f(xs[i]) + 4 * f(xs[i+1]) + f(xs[i+2]))
    return res


def f(x):
    return sqrt(x)

a, b = 1, 1.3
h = 0.05

print(simps_int(f, a, b, h))
