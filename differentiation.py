import sympy as sym

def forward_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h).evalf() - f.subs(sym.Symbol('x'), x).evalf()
    return float(numerator/h)

def backward_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x).evalf() - f.subs(sym.Symbol('x'), x - h).evalf()
    return float(numerator/h)

def centered_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h).evalf() - f.subs(sym.Symbol('x'), x - h).evalf()
    return float(numerator/(2*h))

def second_derivative_centered_difference(f, x, h):
    numerator = f.subs(sym.Symbol('x'), x + h).evalf() - 2*f.subs(sym.Symbol('x'), x).evalf() + f.subs(sym.Symbol('x'), x - h).evalf()
    return float(numerator/(h**2))