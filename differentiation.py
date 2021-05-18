import sympy as sym

def forward_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h) - f.subs(sym.Symbol('x'), x)
    return numerator/h

def backward_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x) - f.subs(sym.Symbol('x'), x - h)
    return numerator/h

def centered_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h) - f.subs(sym.Symbol('x'), x - h)
    return numerator/(2*h)

def second_derivative_centered_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h) - 2*f.subs(sym.Symbol('x'), x) + f.subs(sym.Symbol('x'), x - h)
    return numerator/(h**2)