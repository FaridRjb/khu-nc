#!/usr/bin/env python
# coding: utf-8

from math import sqrt, exp


def gauss_int(f, a, b):

    def g(u):
        
        x = 0.5 * ((b - a) * u + (b + a))
        return f(x)

    u0, u1 = - sqrt(3)/3, sqrt(3)/3
    res = (b - a) / 2 * (g(u0) + g(u1))
    return res


def f(x):
    return x * exp(x)

a, b = 1, 1.3

print(gauss_int(f, a, b))
