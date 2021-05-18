from sys import stdin
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from differentiation import forward_difference, backward_difference, centered_difference, second_derivative_centered_difference

def main():
    x = sym.Symbol('x')
    f1 = x*sym.sin(x**2) + 1
    f2 = sym.cos(x**2) - x**3 + sym.exp(x)
    f3 = sym.sin(sym.pi*x) + x**2 + 2
    f4 = sym.sinh(x)*0.3 + x**3 - sym.exp(x) + sym.pi
    f5 = sym.sin(x**2 + 10)/2**((x**3 -3 + sym.pi/2)/sym.pi)
    functions = [f1, f2, f3, f4, f5]
    # NOTE: If you define a new function, you also need to add it to the functions list in order to use it later on
    i = 1
    for func in functions:
        print(f"{i}. {func}")
        i += 1
    good = False
    option = None
    while(not good):
        option = int(input("Please choose the function you want to work with: ")); option -= 1
        if(option < 0 or option >= len(functions)):
            print("Invalid option. Please try again")
        else:
            good = True
    f = functions[option]
    analytic_der = sym.diff(f, x)
    analytic_second_der = sym.diff(analytic_der, x)
    print(f"f(x) = {f}")
    print(f"df(x)/dx = {analytic_der}")
    print(f"d2f(x)/dx2 = {analytic_second_der}")
    x_values = list(np.linspace(-2, 5, num = 1000))
    f_values = list()
    analytic_der_values = list()
    analytic_second_der_values = list()
    der_values = list()
    second_der_values = list()
    h = 0.1
    for x in x_values:
        f_values.append(f.subs(sym.Symbol('x'), x))
        analytic_der_values.append(analytic_der.subs(sym.Symbol('x'), x))
        analytic_second_der_values.append(analytic_second_der.subs(sym.Symbol('x'), x))
        der_values.append(centered_difference(f, x, h))
        second_der_values.append(second_derivative_centered_difference(f, x, h))

    # Plotting
    fig1, ax1 = plt.subplots()
    # ax1.plot(x_values, f_values, label="Function")
    ax1.plot(x_values, analytic_der_values, label="Analytic derivative")
    ax1.plot(x_values, der_values, label="Numerical derivative")
    ax1.legend()
    ax1.set_xlabel("x")
    ax1.set_ylabel("df(x)/dx")
    # ax1.set_title(f'Analytic and numerical derivative')
    # ax1.grid(True)

    fig2, ax2 = plt.subplots()
    # ax2.plot(x_values, f_values, label="Function")
    ax2.plot(x_values, analytic_second_der_values, label="Analytic second derivative")
    ax2.plot(x_values, second_der_values, label="Numerical second derivative")
    ax2.legend()
    ax2.set_xlabel("x")
    ax2.set_ylabel("d2f(x)/dx2")
    # ax2.set_title(f'Analytic and numerical second derivative')
    # ax2.grid(True)

    plt.show()
    return 0

if __name__ == '__main__':
    main()