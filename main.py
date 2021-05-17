from sys import stdin
import sympy as sym

def main():
    x = sym.Symbol('x')
    f1 = x**2 + sym.sqrt(x**3 + 5) - 1/x
    f2 = sym.tan(sym.sqrt(x**2 - 2) + 10) - sym.log(x + 3)
    f3 = sym.exp(x**2 - sym.sqrt(x + 2)) - sym.cos(x**2)
    f4 = sym.sin(x) + x**2/(x - 3)
    print("ANALYTICAL DERIVATIVES")
    print("-------------------------------------------------------")
    print("f1: ", f1)
    print("df1/dx: ", sym.diff(f1, x))
    print("-------------------------------------------------------")
    print("f2: ", f1)
    print("df2/dx: ", sym.diff(f2, x))
    print("-------------------------------------------------------")
    print("f3: ", f1)
    print("df3/dx: ", sym.diff(f3, x))
    print("-------------------------------------------------------")
    print("f4: ", f1)
    print("df4/dx: ", sym.diff(f4, x))
    print("-------------------------------------------------------")

    return 0

if __name__ == '__main__':
    main()