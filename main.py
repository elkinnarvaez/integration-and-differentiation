from sys import stdin
import sympy as sym

def main():
    x = sym.Symbol('x')
    f1 = x**2 + sym.sqrt(x**3 + 5) - 1/x
    df1 = sym.diff(f1, x)
    f2 = sym.tan(sym.sqrt(x**2 - 2) + 10) - sym.log(x + 3)
    df2 = sym.diff(f2, x)
    f3 = sym.exp(x**2 - sym.sqrt(x + 2)) - sym.cos(x**2)
    df3 = sym.diff(f3, x)
    f4 = sym.sin(x) + x**2/(x - 3)
    df4 = sym.diff(f4, x)
    print("ANALYTICAL DERIVATIVES")
    print("-------------------------------------------------------")
    print("f1: ", f1)
    print("df1/dx: ", df1)
    print("-------------------------------------------------------")
    print("f2: ", f2)
    print("df2/dx: ", df2)
    print("-------------------------------------------------------")
    print("f3: ", f3)
    print("df3/dx: ", df3)
    print("-------------------------------------------------------")
    print("f4: ", f4)
    print("df4/dx: ", df4)
    print("-------------------------------------------------------")

    return 0

if __name__ == '__main__':
    main()