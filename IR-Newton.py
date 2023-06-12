#!/usr/bin/env python
# coding: utf-8

from math import sqrt


def newt_int(f, a, b):

    h = (b - a) / 3
    res = (3*h/8) * (f(a + 0*h) + 3*f(a + 1*h) \
                     + 3*f(a + 2*h) + f(a + 3*h))
    return res


def f(x):
    return sqrt(x)

a, b = 1, 1.3

print(newt_int(f, a, b))
