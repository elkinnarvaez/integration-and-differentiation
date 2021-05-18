from sys import stdin
import sympy as sym
import numpy as np

def main():
    x = sym.Symbol('x')
    f1 = x**2 + sym.sqrt(x**3 + 5) - 1/x
    analytic_diff1 = sym.diff(f1, x)
    f2 = sym.tan(sym.sqrt(x**2 - 2) + 10) - sym.log(x + 3)
    analytic_diff2 = sym.diff(f2, x)
    f3 = sym.exp(x**2 - sym.sqrt(x + 2)) - sym.cos(x**2)
    analytic_diff3 = sym.diff(f3, x)
    f4 = sym.sin(x) + x**2/(x - 3)
    analytic_diff4 = sym.diff(f4, x)
    functions = [(f1, analytic_diff1), (f2, analytic_diff2), (f3, analytic_diff3), (f4, analytic_diff4)]
    # print("ANALYTIC DERIVATIVES")
    # print("-------------------------------------------------------")
    # print("f1:", f1)
    # print("df1/dx:", analytic_diff1)
    # print("-------------------------------------------------------")
    # print("f2:", f2)
    # print("df2/dx:", analytic_diff2)
    # print("-------------------------------------------------------")
    # print("f3:", f3)
    # print("df3/dx:", analytic_diff3)
    # print("-------------------------------------------------------")
    # print("f4:", f4)
    # print("df4/dx:", analytic_diff4)
    # print("-------------------------------------------------------")
    i = 1
    for func in functions:
        print(f"{i}. {func[0]}")
        i += 1
    good = False
    option = None
    while(not good):
        option = int(input("Please choose the function you want to work with: ")); option -= 1
        if(option < 0 or option >= len(functions)):
            print("Invalid option. Please try again")
        else:
            good = True
    f = functions[option][0]
    analytic_diff = functions[option][1]
    x_values = list(np.linspace(-10, 10, num = 1000))
    f_values = list()
    analytic_diff_values = list()
    for value in x_values:
        f_values.append(f.subs(x, value))
        analytic_diff_values.append(analytic_diff.subs(x, value))
    return 0

if __name__ == '__main__':
    main()