import sympy as sym
import numpy as np

def rectangle_rule(f, a, b):
    w1 = (b - a)
    return w1*(f.subs(sym.Symbol('x'), (a + b)/2).evalf())

def trapezoid_rule(f, a, b):
    w1 = (b - a)/2
    w2 = (b - a)/2
    return w1*(f.subs(sym.Symbol('x'), a).evalf()) + w2*(f.subs(sym.Symbol('x'), b).evalf())

def simpsons_rule(f, a, b):
    w1 = (b - a)/6
    w2 = 4*(b - a)/6
    w3 = (b - a)/6
    return w1*(f.subs(sym.Symbol('x'), a).evalf()) + w2*(f.subs(sym.Symbol('x'), (a + b)/2).evalf()) + w3*(f.subs(sym.Symbol('x'), b).evalf())

def composite_rectangle_rule(f, a, b, n):
    ans = 0
    x = list(np.linspace(a, b, num = n))
    for i in range(0, n - 1):
        ans += rectangle_rule(f, x[i], x[i + 1])
    return ans

def composite_trapezoid_rule(f, a, b, n):
    ans = 0
    x = list(np.linspace(a, b, num = n))
    for i in range(0, n - 1):
        ans += trapezoid_rule(f, x[i], x[i + 1])
    return ans

def composite_simpsons_rule(f, a, b, n):
    ans = 0
    x = list(np.linspace(a, b, num = n))
    for i in range(0, n - 1):
        ans += simpsons_rule(f, x[i], x[i + 1])
    return ans